"""Independent stdlib synthetic calculations only; never executes a producer/host/device."""
import base64
import copy
import hashlib
import json
from pathlib import Path
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", newline="\n")
sys.stderr.reconfigure(encoding="utf-8", newline="\n")

HERE = Path(__file__).resolve().parent
FIXED_CONFIG = '/home/root/.config/remarkable-buddies/config.json'
ROOT = next(p for p in HERE.parents if (p/'openspec/specs').is_dir())
FROZEN = ROOT/'openspec/changes/archive/2026-10-23-prepare-source-cache-slot-cleanup/digest-vectors.json'
FIELDS = 'report_version operation status runtime_unverified possible_effect document intent entry_bytes entry_sha256'.split()
ORDER = 'intent_version operation document config_path_sha256 config_bytes_sha256 roots_sha256 actor generation store_owner_sha256 cache_owner_sha256 namespace_owner_sha256 namespace_identity_sha256 entry_identity_sha256 entry_bytes entry_sha256'.split()
DOC = '22222222-2222-4222-8222-222222222222'
OP = '11111111-1111-4111-8111-111111111111'
BOOT = '55555555-5555-4555-8555-555555555555'
IDENTITY = {'connection_id': 'a'*64, 'boot_id': BOOT}

def sha(b):
    return hashlib.sha256(b).hexdigest()

def frame(domain, parts):
    out = domain.encode('ascii')+b'\0'
    for part in parts:
        raw = str(part).encode('utf-8')
        out += len(raw).to_bytes(8, 'little')+raw
    return sha(out)

def wire(v):
    return json.dumps(v, separators=(',', ':'), ensure_ascii=False).encode("utf-8")+b'\n'

def uuid(v):
    return isinstance(v, str) and re.fullmatch('[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}', v) and v != '00000000-0000-0000-0000-000000000000'

def digest(v):
    return isinstance(v, str) and re.fullmatch('[0-9a-f]{64}', v)

def exact(v, fields):
    assert isinstance(v, dict) and set(v) == set(fields)

intent = dict(intent_version=1, operation=OP, document=DOC,
              config_path_sha256=frame('buddy-cache-config-path-v1', [FIXED_CONFIG]),
              config_bytes_sha256='1'*64, roots_sha256='2'*64,
              actor='33333333-3333-4333-8333-333333333333',
              generation='44444444-4444-4444-8444-444444444444',
              store_owner_sha256='3'*64, cache_owner_sha256='4'*64,
              namespace_owner_sha256='5'*64, namespace_identity_sha256='6'*64,
              entry_identity_sha256='7'*64, entry_bytes=123, entry_sha256='8'*64)

def rehash(i):
    i['intent_sha256'] = frame('buddy-source-cache-cleanup-intent-v1', [i[k] for k in ORDER])
    return i

rehash(intent)

class Future(Exception):
    pass

def admit(raw, selector):
    assert len(raw) <= 16384 and raw.endswith(b'\n') and raw.count(b'\n') == 1
    def pairs(items):
        obj = {}
        for k, value in items:
            assert k not in obj
            obj[k] = value
        return obj
    r = json.loads(raw.decode('utf-8'), object_pairs_hook=pairs,
                   parse_constant=lambda _: (_ for _ in ()).throw(AssertionError()))
    assert isinstance(r, dict) and type(r.get('report_version')) is int and r['report_version'] >= 1
    if r['report_version'] != 1:
        raise Future()
    exact(r, FIELDS)
    assert r['operation'] == selector and selector in ('prepare', 'apply', 'status')
    assert r['runtime_unverified'] is True and type(r['possible_effect']) is bool
    status = r['status']
    allowed = {'prepare': ['prepared', 'absent', 'conflict', 'unavailable', 'busy', 'unsupported', 'invalid-input'],
               'apply': ['applied', 'unknown', 'absent', 'conflict', 'unavailable', 'busy', 'unsupported', 'invalid-input'],
               'status': ['unchanged', 'absent', 'conflict', 'unavailable', 'busy', 'unsupported', 'invalid-input']}
    assert status in allowed[selector]
    assert r['possible_effect'] == (selector == 'apply' and status in ('applied', 'unknown'))
    assert r['document'] == DOC or (status in ('unsupported', 'invalid-input') and r['document'] is None)
    if status == 'invalid-input':
        assert r['document'] is None
    present = r['entry_bytes'] is not None or r['entry_sha256'] is not None
    if present:
        assert type(r['entry_bytes']) is int and 1 <= r['entry_bytes'] <= 33554432 and digest(r['entry_sha256'])
    if status in ('prepared', 'applied', 'unknown', 'unchanged'):
        assert present
    elif status == 'conflict' and selector != 'prepare':
        pass
    else:
        assert not present
    if status == 'prepared':
        i = r['intent']
        exact(i, ORDER+['intent_sha256'])
        assert type(i['intent_version']) is int and i['intent_version'] == 1
        assert i['operation'] == OP and i['document'] == DOC and uuid(i['actor']) and uuid(i['generation'])
        assert all(digest(i[k]) for k in ORDER if k.endswith('_sha256'))
        assert i['config_path_sha256'] == frame('buddy-cache-config-path-v1', [FIXED_CONFIG])
        assert i['intent_sha256'] == frame('buddy-source-cache-cleanup-intent-v1', [i[k] for k in ORDER])
        assert type(i['entry_bytes']) is int and 1 <= i['entry_bytes'] <= 33554432
        assert i['entry_bytes'] == r['entry_bytes'] and i['entry_sha256'] == r['entry_sha256']
    else:
        assert r['intent'] is None
    if status in ('applied', 'unknown', 'unchanged'):
        assert r['entry_bytes'] == intent['entry_bytes'] and r['entry_sha256'] == intent['entry_sha256']
    state = {'prepare': {'prepared': 'ready', 'absent': 'absent', 'busy': 'busy', 'unsupported': 'unsupported'},
             'apply': {'applied': 'applied', 'unknown': 'unknown', 'absent': 'absent'},
             'status': {'unchanged': 'unchanged', 'absent': 'absent-observed', 'conflict': 'conflict', 'busy': 'busy', 'unsupported': 'unsupported'}}[selector].get(status, 'not-dispatched' if selector == 'apply' else 'unavailable')
    return dict(state=state, preview={'document': DOC, 'entry_bytes': r['entry_bytes']} if state == 'ready' else None,
                report={k: r[k] for k in ['operation', 'status', 'runtime_unverified', 'possible_effect']})

def report(selector, status, pair='auto', early=False):
    present = status in ('prepared', 'applied', 'unknown', 'unchanged') or pair in ('changed', 'same')
    return dict(report_version=1, operation=selector, status=status, runtime_unverified=True,
                possible_effect=selector == 'apply' and status in ('applied', 'unknown'),
                document=None if early or status == 'invalid-input' else DOC,
                intent=copy.deepcopy(intent) if status == 'prepared' else None,
                entry_bytes=124 if pair == 'changed' else 123 if present else None,
                entry_sha256='9'*64 if pair == 'changed' else '8'*64 if present else None)

valid = []
for selector, statuses in [('prepare', ['prepared', 'absent', 'conflict', 'unavailable', 'busy', 'unsupported', 'invalid-input']),
                           ('apply', ['applied', 'unknown', 'absent', 'conflict', 'unavailable', 'busy', 'unsupported', 'invalid-input']),
                           ('status', ['unchanged', 'absent', 'conflict', 'unavailable', 'busy', 'unsupported', 'invalid-input'])]:
    for status in statuses:
        valid.append((f'{selector}-{status}', selector, wire(report(selector, status))))
        if status == 'unsupported':
            valid.append((f'{selector}-unsupported-early', selector, wire(report(selector, status, early=True))))
        if status == 'conflict' and selector != 'prepare':
            for pair in ('changed', 'same'):
                valid.append((f'{selector}-conflict-{pair}', selector, wire(report(selector, status, pair))))
prepared = wire(report('prepare', 'prepared'))
valid.append(('prepare-inclusive16384', 'prepare', prepared[:-1]+b' '*(16384-len(prepared))+b'\n'))
negative = []
def mutate(name, selector, change, base=None):
    r = copy.deepcopy(base if base is not None else report(selector, {'prepare': 'prepared', 'apply': 'applied', 'status': 'unchanged'}[selector]))
    change(r)
    negative.append((name, selector, wire(r)))
for selector in ('prepare', 'apply', 'status'):
    for name, change in [('unknown-key', lambda r:r.update(raw='SYNTHETIC_PRIVATE')),
                         ('wrong-operation', lambda r:r.update(operation='inspect')),
                         ('nil-document', lambda r:r.update(document='00000000-0000-0000-0000-000000000000')),
                         ('uppercase-document', lambda r:r.update(document='AAAAAAAA-AAAA-4AAA-8AAA-AAAAAAAAAAAA')),
                         ('runtime-false', lambda r:r.update(runtime_unverified=False)),
                         ('effect-wrong', lambda r:r.update(possible_effect=not r['possible_effect'])),
                         ('size-zero', lambda r:r.update(entry_bytes=0)),
                         ('size-bool', lambda r:r.update(entry_bytes=True)),
                         ('size-fraction', lambda r:r.update(entry_bytes=1.5)),
                         ('size-over', lambda r:r.update(entry_bytes=33554433)),
                         ('size-unsafe', lambda r:r.update(entry_bytes=9007199254740992)),
                         ('missing-hash', lambda r:r.update(entry_sha256=None)),
                         ('hash-upper', lambda r:r.update(entry_sha256='A'*64)),
                         ('refusal-with-pair', lambda r:r.update(status='unavailable',possible_effect=False,intent=None))]:
        mutate(selector+'-'+name, selector, change)
    forbidden = {'prepare':['ready','applied','unknown','unchanged'],'apply':['ready','prepared','unchanged'],'status':['ready','prepared','applied','unknown']}[selector]
    for status in forbidden:
        mutate(selector+'-wrong-status-'+status, selector, lambda r,status=status:r.update(status=status))
for name, fn in [('hash-mismatch',lambda i:i.update(intent_sha256='0'*64)),
                 ('extra-intent',lambda i:i.update(path='SYNTHETIC_PRIVATE')),
                 ('wrong-selected',lambda i:rehash(dict(i,document=BOOT))),
                 ('wrong-operation-id',lambda i:rehash(dict(i,operation=BOOT))),
                 ('nil-actor',lambda i:rehash(dict(i,actor='00000000-0000-0000-0000-000000000000'))),
                 ('wrong-fixed-config',lambda i:rehash(dict(i,config_path_sha256='0'*64))),
                 ('wrong-bound-size',lambda i:rehash(dict(i,entry_bytes=124))),
                 ('fractional-intent-size',lambda i:rehash(dict(i,entry_bytes=123.0)))]:
    def change(r,fn=fn):
        updated=fn(r['intent'])
        if updated is not None:r['intent']=updated
    mutate('intent-'+name,'prepare',change)
for selector in ('prepare','apply','status'):
    mutate(selector+'-invalid-document-present',selector,lambda r:r.update(status='invalid-input',possible_effect=False,intent=None,entry_bytes=None,entry_sha256=None))
raw_bad = [('missing-LF',prepared[:-1]),('two-reports',prepared+prepared),('UTF8-invalid',b'\xff\n'),('BOM',b'\xef\xbb\xbf'+prepared),('empty',b''),('over16385',prepared[:-1]+b' '*(16385-len(prepared))+b'\n'),('duplicate-top',prepared.replace(b'"report_version":1',b'"report_version":1,"report_version":1')),('duplicate-nested',prepared.replace(b'"intent_version":1',b'"intent_version":1,"intent_version":1'))]
negative.extend((name,'prepare',b)for name,b in raw_bad)

def row(name, selector, raw, expected):
    return dict(name=name,selector=selector,hex=raw.hex(),utf8_bytes=len(raw),sha256=sha(raw),expected=expected)
valid_rows = [row(n,s,b,admit(b,s)) for n,s,b in valid]
negative_rows = []
for n,s,b in negative:
    try:
        admit(b,s)
    except (AssertionError,ValueError,UnicodeError,KeyError,TypeError):
        negative_rows.append(row(n,s,b,{'state':'unknown' if s=='apply' else 'unavailable','report':None,'preview':None}))
    else:
        raise AssertionError('negative unexpectedly admitted: '+n)
future=[]
for selector in ('prepare','apply','status'):
    b=wire(dict(report_version=2))
    try:admit(b,selector)
    except Future:future.append(row(selector+'-future',selector,b,{'state':'unknown' if selector=='apply' else 'unsupported','report':None,'preview':None}))
old=json.loads(FROZEN.read_text(encoding="utf-8"))
for r in old['vectors']:assert frame(r['domain'],r['parts'])==r['sha256']
lanes=['model','basic','forget','ordinary-export','research-settings','memory-settings','credential-reference','model-credential','source-cache-inventory','source-cache-cleanup']
pairs=[dict(first=a,second=b,old72='source-cache-cleanup' not in (a,b),expected='busy without hooks/cancel/I/O/grant/original/timer changes; late token cannot revoke newer owner')for a in lanes for b in lanes if a!=b]
assert len(pairs)==90 and sum(p['old72']for p in pairs)==72
boundaries=[]
for names in [('beginModel','saveModel','checkModel'),('beginBasic','saveBasic','checkBasic'),('beginResearch','saveResearch','checkResearch'),('beginSavedMemory','saveMemorySettings','checkMemorySettings'),('beginCredential','saveCredential','checkCredential'),('beginFileCredential','saveFileCredential','checkFileCredential'),('prepareExport','confirmExport','checkExport')]:
    boundaries.extend(dict(method=n,argument=None)for n in names)
boundaries += [dict(method='prepareForget',argument=None),dict(method='forgetAction',argument='confirm'),dict(method='forgetAction',argument='status'),dict(method='inspectSourceCache',argument=None)]
assert len(boundaries)==25
INV = '66666666-6666-4666-8666-666666666666'
requests=[{'action':'retained'},{'action':'cancel','reference':'f'*64,'invocation':INV},{'action':'prepare',**IDENTITY,'document':DOC,'invocation':INV}]+[{'action':a,**IDENTITY,'reference':'f'*64,'invocation':INV}for a in ['confirm','status']]
def public_request(raw):
    assert len(raw)<=384
    def pairs(items):
        obj={}
        for key,value in items:
            assert key not in obj
            obj[key]=value
        return obj
    q=json.loads(raw.decode('utf-8'),object_pairs_hook=pairs)
    action=q.get('action') if isinstance(q,dict)else None
    fields={'retained':['action'],'cancel':['action','reference','invocation'],'prepare':['action','connection_id','boot_id','document','invocation'],'confirm':['action','connection_id','boot_id','reference','invocation'],'status':['action','connection_id','boot_id','reference','invocation']}
    assert action in fields
    exact(q,fields[action])
    if action!='retained':assert uuid(q['invocation'])
    if action in ('cancel','confirm','status'):assert digest(q['reference'])
    if action in ('prepare','confirm','status'):assert digest(q['connection_id']) and uuid(q['boot_id'])
    if action=='prepare':assert uuid(q['document'])
    return q
public=[dict(request=q,utf8_bytes=len(wire(q))-1)for q in requests]
for row_ in public:assert public_request(wire(row_['request'])[:-1])==row_['request']
padded=wire(requests[0])[:-1];assert public_request(padded+b' '*(384-len(padded)))==requests[0]
public_invalid=[]
for q in requests[1:]:
    for label,changes in [('missing-invocation',None),('nil-invocation','00000000-0000-0000-0000-000000000000'),('uppercase-invocation','AAAAAAAA-AAAA-4AAA-8AAA-AAAAAAAAAAAA'),('numeric-invocation',1)]:
        bad=copy.deepcopy(q)
        if changes is None:bad.pop('invocation')
        else:bad['invocation']=changes
        raw=wire(bad)[:-1]
        try:public_request(raw)
        except (AssertionError,ValueError,UnicodeError,TypeError):public_invalid.append(dict(name=q['action']+'-'+label,hex=raw.hex(),bytes=len(raw),sha256=sha(raw),expected='refused'))
        else:raise AssertionError('public request unexpectedly valid')
for label,raw in [('over385',padded+b' '*(385-len(padded))),('duplicate-invocation',wire(requests[1])[:-1].replace(b'"invocation":',b'"invocation":"'+INV.encode("utf-8")+b'","invocation":'))]:
    try:public_request(raw)
    except (AssertionError,ValueError,UnicodeError,TypeError):public_invalid.append(dict(name=label,hex=raw.hex(),bytes=len(raw),sha256=sha(raw),expected='refused'))
    else:raise AssertionError(label)

# Bounded independent state calculation, NOT a Manager coordinator/transport.
def nonce(label):
    if uuid(label):return label
    raw=bytearray(hashlib.sha256(('SYNTHETIC:'+label).encode("utf-8")).digest()[:16]);raw[6]=(raw[6]&15)|64;raw[8]=(raw[8]&63)|128
    h=raw.hex();return f'{h[:8]}-{h[8:12]}-{h[12:16]}-{h[16:20]}-{h[20:]}'
class InvocationModel:
    def __init__(self,ready=False):
        self.ref='f'*64;self.valid=True;self.prepare=nonce('prepare-inv');self.ledger={self.prepare:'ready' if ready else 'completed'}
        if not ready:self.ledger[nonce('confirm-inv')]='completed'
        self.ready=ready;self.active=None;self.sequence=0;self.calls=0;self.cancels=0;self.releases=0;self.hooks=0;self.erases=0;self.deadline=1800000;self.editor='newer-editor'
    def snapshot(self):
        return dict(reference_valid=self.valid,active=copy.deepcopy(self.active),raw_calls=self.calls,raw_cancels=self.cancels,releases=self.releases,hooks=self.hooks,erasures=self.erases,original_deadline=self.deadline,editor=self.editor,ledger_entries=len(self.ledger))
    def admit(self,inv,operation='status'):
        inv=nonce(inv)
        if not self.valid:return 'unavailable'
        if inv in self.ledger:return 'reused-or-fenced'
        if operation=='confirm' and not self.ready:return 'unavailable'
        if operation=='status' and self.ready:return 'unavailable'
        if self.active:return 'busy'
        if len(self.ledger)>=32:return 'capacity'
        self.sequence+=1;self.active={'ref':self.ref,'invocation':inv,'token':self.sequence,'operation':operation};self.ledger[inv]='active';self.calls+=1;self.hooks+=1
        if operation=='confirm':self.ready=False;self.ledger[self.prepare]='completed'
        return 'admitted'
    def finish(self):
        self.ledger[self.active['invocation']]='completed';self.active=None
    def cancel(self,ref,inv):
        inv=nonce(inv)
        if not self.valid or ref!=self.ref:return 'unavailable'
        phase=self.ledger.get(inv)
        if phase=='active' and self.active and self.active['invocation']==inv:
            self.cancels+=1;self.releases+=1;self.ledger[inv]='cancelled';self.active=None;return 'unknown'
        if phase=='ready' and self.ready and inv==self.prepare:
            self.ready=False;self.valid=False;self.ledger={};self.erases+=1;return 'invalidated'
        if phase is not None:return 'unavailable'
        if len(self.ledger)>=32:return 'unavailable'
        self.ledger[inv]='fenced';return 'not-dispatched'
invocation_cases=[]
for transport in ['HTTP-before-guarded-handler','IPC-before-guarded-handler']:
    m=InvocationModel();assert m.admit('old-status')=='admitted';queued={'reference':m.ref,'invocation':nonce('old-status')};m.finish();assert m.admit('new-status-same-original')=='admitted';before=m.snapshot();outcome=m.cancel(queued['reference'],queued['invocation']);after=m.snapshot();assert before==after and outcome=='unavailable'
    invocation_cases.append(dict(name=transport+'-old-stop14s-then-new-same-reference',captured_before_queue=queued,steps=['hold old cancel before real handler','finish old status','local Stop wait expires at14000','admit new status with fresh invocation on SAME original','release old cancel'],before=before,after=after,outcome=outcome,required_actual_execution=True))
for old_inv,new_inv in [('confirm-inv','new-status'),('prepare-inv','new-confirm')]:
    m=InvocationModel(ready=old_inv=='prepare-inv');assert m.admit(new_inv,'confirm' if new_inv=='new-confirm'else 'status')=='admitted';before=m.snapshot();assert m.cancel(m.ref,old_inv)=='unavailable'and m.snapshot()==before
    invocation_cases.append(dict(name='completed-'+old_inv+'-does-not-cancel-'+new_inv,before=before,after=m.snapshot()))
for operation in ['confirm','status']:
    m=InvocationModel(ready=operation=='confirm');assert m.cancel(m.ref,'queued-operation')=='not-dispatched';before=m.snapshot();assert m.admit('queued-operation',operation)=='reused-or-fenced'and m.snapshot()==before
    invocation_cases.append(dict(name='cancel-before-'+operation+'-fences-only-that-invocation',before=before,after=m.snapshot()))
m=InvocationModel();assert m.admit('old-status')=='admitted';m.finish();before=m.snapshot();assert m.admit('old-status')=='reused-or-fenced'and m.snapshot()==before;invocation_cases.append(dict(name='completed-invocation-never-reused',before=before,after=m.snapshot()))
m=InvocationModel()
for n in range(29):assert m.admit('completed-'+str(n))=='admitted';m.finish()
assert m.admit('last-active')=='admitted'and len(m.ledger)==32;before=m.snapshot();assert m.admit('over-cap')=='busy'and m.snapshot()==before;assert m.cancel(m.ref,'unseen-cancel')=='unavailable'and m.snapshot()==before;assert m.cancel(m.ref,'last-active')=='unknown';after_cancel=m.snapshot();assert m.admit('over-cap')=='capacity'and m.snapshot()==after_cancel;invocation_cases.append(dict(name='32-entry-cap-no-eviction-current-cancel-still-works',before=before,after=after_cancel))
m=InvocationModel();assert m.admit('status')=='admitted';before=m.snapshot();assert m.cancel('e'*64,'status')=='unavailable'and m.snapshot()==before;invocation_cases.append(dict(name='other-reference-cancel-zero-effect',before=before,after=m.snapshot()))
m=InvocationModel(ready=True);before=m.snapshot();assert m.cancel(m.ref,m.prepare)=='invalidated'and m.cancels==0 and m.releases==0;assert m.admit('late-confirm','confirm')=='unavailable';invocation_cases.append(dict(name='matching-idle-ready-origin-only',before=before,after=m.snapshot()))
vectors=dict(basis='Independent synthetic reference calculations only; no producer/Manager/device execution. All names/IDs/hashes fictitious and not authority.',private_intent=intent,valid=valid_rows,invalid=negative_rows,future=future,public_request_sizes=public,public_invalid=public_invalid,public_cap=384,invocation_cases=invocation_cases,invocation_ledger_cap=32,total_nonce_bound=288,owner_pairs=pairs,peer_boundaries=boundaries,extra_forget_receipt_boundary={'method':'forgetAction','argument':'receipt'},outgoing_clear_recipes=[{'cleanup_action':a,'peer':p}for a in ['prepare','confirm','status']for p in lanes if p!='source-cache-cleanup'],frozen_producer_vectors_recomputed=len(old['vectors']))
(HERE/'vectors.json').write_text(json.dumps(vectors,indent=2)+'\n', encoding="utf-8", newline="\n")
print(json.dumps(dict(valid=len(valid_rows),invalid=len(negative_rows),future=len(future),owner_pairs=len(pairs),old72=72,peer_boundaries=len(boundaries),outgoing_clear=27,producer_encoding_vectors=7,public_invalid=len(public_invalid),invocation_reference_cases=len(invocation_cases),execution='reference calculations only')))
