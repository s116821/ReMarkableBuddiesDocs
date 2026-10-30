"""Literal independent proposed oracles; no consumer/producer implementation imported."""
from pathlib import Path
import copy,hashlib,json
p=Path(__file__).resolve().parent
cp=copy.deepcopy
uid=lambda n:f'{n:08x}-1111-4111-8111-{n:012x}'
cid='a'*64;boot=uid(7);ref='b'*64;inv=uid(1);path='/home/root/backups/selected-history'
summary={'format':2,'manifests':2,'objects':7,'selected_scopes':1,'selection_receipts':2,'complete_media':True,'configuration_included':False}
def report(op='inspect',status='ok',s=None):
 s=cp(summary if s is None else s)
 return {'report_version':1,'operation':op,'status':status,'incomplete':not s['complete_media'] if status=='ok' else status in ['unavailable','failed'],'activation_performed':False,'data':{'inspection':s} if status=='ok' else None}
def dump(o):return json.dumps(o,separators=(',',':'),ensure_ascii=True)
raw=[]
def rawcase(id,value,expect,basis,op='inspect',text=None,hexbytes=None):
 b=bytes.fromhex(hexbytes) if hexbytes is not None else (text if text is not None else dump(value)+'\n').encode()
 row={'id':id,'operation':op,'expect':expect,'basis':basis,'stdout_bytes':len(b),'stdout_sha256':hashlib.sha256(b).hexdigest()}
 if hexbytes is not None:row['stdout_hex']=hexbytes
 else:row['stdout_utf8']=b.decode()
 raw.append(row)
for f in [1,2,3]:
 for complete in [True,False]:
  s=cp(summary);s.update(format=f,complete_media=complete)
  if f!=2:s.update(selected_scopes=0,selection_receipts=0,configuration_included=True)
  rawcase(f'inspect-format{f}-{complete}',report(s=s),'accept','Pinned whole-archive validator supports this format and media truth')
for complete in [True,False]:
 s=cp(summary);s['complete_media']=complete
 rawcase(f'export-selected-{complete}',report('export-selected',s=s),'accept','Export only format2, settings excluded','export-selected')
for op,statuses in [('inspect',['invalid-input','unavailable','unsupported']),('export-selected',['invalid-input','unavailable','unsupported','busy','failed'])]:
 for status in statuses:rawcase(f'{op}-{status}',report(op,status),'accept','Exact refusal incomplete/data truth',op)
base=report()
for id,key,value in [('wrong-version','report_version',2),('wrong-operation','operation','export-selected'),('activation-claim','activation_performed',True),('numeric-incomplete','incomplete',0),('bad-status','status','complete'),('success-with-null','data',None),('false-incomplete','incomplete',True)]:
 v=cp(base);v[key]=value;rawcase(id,v,'refuse','Closed header/phase relation')
v=cp(base);v['token']='SYNTHETIC_PRIVATE_SENTINEL';rawcase('extra-private-key',v,'refuse','No extra/raw credential fields')
for op in ['inspect','export-selected']:
 v=report(op,'unsupported');v['data']=cp(base['data']);rawcase(op+'-refusal-with-data',v,'refuse','Refusal cannot carry success',op)
 v=report(op,'unavailable');v['incomplete']=False;rawcase(op+'-wrong-unavailable-flag',v,'refuse','Exact flag mapping',op)
for status in ['busy','failed']:rawcase('inspect-impossible-'+status,report('inspect',status),'refuse','Current inspect code never emits this phase')
for field,value in [('format',0),('format',4),('format',99),('manifests',-1),('objects',4097),('objects',1.5),('selected_scopes',0),('selection_receipts',4097),('complete_media','yes'),('configuration_included',True)]:
 v=cp(base);v['data']['inspection'][field]=value;rawcase(f'bad-summary-{field}-{value}',v,'refuse','Exact supported types/bounds/format2 relation')
for f in [1,3]:
 s=cp(summary);s.update(format=f,selected_scopes=0,selection_receipts=0)
 rawcase(f'export-wrong-format{f}',report('export-selected',s=s),'refuse','Selected export cannot claim another format','export-selected')
 s['selected_scopes']=1;rawcase(f'nonselected-format{f}-has-scope',report(s=s),'refuse','Nonselected format cannot carry selected counts')
v=cp(base);v['data']['inspection']['path']=path;rawcase('private-summary-path',v,'refuse','No path in reduced summary')
text=dump(base)
rawcase('duplicate-root',None,'refuse','Duplicate keys at any depth',text=text.replace('"report_version":1','"report_version":1,"report_version":1')+'\n')
rawcase('duplicate-nested',None,'refuse','Nested duplicate keys',text=text.replace('"objects":7','"objects":7,"objects":7')+'\n')
for id,t in [('missing-lf',text),('double-line',text+'\n'+text+'\n'),('crlf-line',text+'\r\n'),('trailing-json',text+' {}\n'),('bom','\ufeff'+text+'\n'),('prefix',text[:40]+'\n')]:rawcase(id,None,'refuse','Exact UTF8 one-line framing',text=t)
rawcase('noncanonical-spaces',None,'accept','Harmless JSON spaces not canonicalized',text=json.dumps(base,indent=None)+'  \n')
rawcase('invalid-utf8',None,'refuse','Invalid UTF8 never replacement-decoded',hexbytes='ff0a')
for size,expect in [(16384,'accept'),(16385,'refuse')]:rawcase('report-bytes-'+str(size),None,expect,'Inclusive raw report cap',text=text+' '*(size-len(text.encode())-1)+'\n')
s=cp(summary);s.update(manifests=4096,objects=4096,selected_scopes=4096,selection_receipts=4096);rawcase('count-exact-bound',report(s=s),'accept','Independent count bounds, no invented arithmetic')
request=[]
def req(action,**kw):return {'action':action,'connection_id':cid,'boot_id':boot,'invocation':inv,**kw}
def rq(id,q,expect,basis):request.append({'id':id,'request':q,'expect':expect,'basis':basis})
for action in ['inspect','prepare-export']:rq(action+'-valid',req(action,path=path),'accept','Initial bounded untrusted path only')
for action in ['confirm-export','check-export']:rq(action+'-valid',req(action,reference=ref),'accept','Opaque original only')
rq('cancel-exact-target',req('cancel',reference=ref),'accept','Cancel names existing executing invocation')
rq('cancel-before-reference',req('cancel',reference=None),'accept','Exact invocation fencing before known host reference')
rq('retained-valid',{'action':'retained'},'accept','Local safe metadata only')
for id,value in [('root','/'),('relative','backup/x'),('nul','/a\0b'),('surrogate','/a\ud800'),('path-over','/'+'x'*4096)]:rq('path-'+id,req('inspect',path=value),'refuse','Scalar path admission')
rq('path-exact',req('inspect',path='/'+'x'*4095),'accept','4096inclusive UTF8 bytes')
rq('path-opaque-crlf',req('prepare-export',path='/a\r\n '),'accept','Exact protected path, no trim/normalization')
for action in ['confirm-export','check-export','cancel']:
 q=req(action,reference=ref,path=path);rq(action+'-substitute-path',q,'refuse','Original-only followup, closed keys')
 q=req(action,reference=ref,intent={'operation':inv});rq(action+'-substitute-intent',q,'refuse','No caller conditions')
for id,q in [('bad-reference',req('confirm-export',reference=uid(9))),('bad-invocation',req('inspect',path=path,invocation='0'*36)),('uppercase-identity',req('inspect',path=path,connection_id='A'*64)),('retained-with-identity',{'action':'retained','connection_id':cid}),('unknown-action',req('restore',path=path))]:rq(id,q,'refuse','Exact shape/identity/action')
rq('renderer-cannot-supply-expected-history',req('check-export',reference=ref,expected_original_outcome='unknown'),'refuse','Expected history belongs only to private response context')
old=json.loads((p.parent/'archive/2026-10-28-restore-ordinary-archive-companion/vectors.json').read_text());obs=cp(old['public_cases'][0]['result']['observation']);obs.update(connection_id=cid,boot_id=boot)
def row(outcome='unknown',expired=False):return {'reference':ref,'connection_id':cid,'boot_id':boot,'original_outcome':outcome,'expired':expired}
def result(state,action,original=None,check=None,s=None):
 retained=[] if original is None else [row(original)]
 return {'contract_version':1,'status':'observed','observation':cp(obs),'selected_archive':{'state':state,'reference':ref,'invocation':inv,'summary':cp(s),'original_outcome':original,'check_outcome':check,'retained':retained}}
public=[]
def pub(id,q,v,expect,basis,expected_original='unknown'):
 c={'id':id,'request':q,'result':v,'expect':expect,'basis':basis}
 if q['action']=='check-export':c['response_context']={**{k:q[k] for k in ['action','reference','connection_id','boot_id','invocation']},'expected_original_outcome':expected_original,'source':'Previously retained immutable original captured privately before awaiting, not renderer authority or returned data'}
 public.append(c)
prep=req('prepare-export',path=path);confirm=req('confirm-export',reference=ref);check=req('check-export',reference=ref);inspect=req('inspect',path=path)
ready=result('ready','prepare-export');pub('ready-policy-only',prep,ready,'accept','No producer counts/receipt')
v=cp(ready);v['selected_archive']['summary']=cp(summary);pub('ready-invented-counts',prep,v,'refuse','Preview has no frozen data')
for state,original,checkval,q in [('inspected',None,None,inspect),('exported','exported',None,confirm),('archive-observed','unknown','archive-observed',check)]:pub(state+'-valid',q,result(state,q['action'],original,checkval,summary),'accept','Phase-specific current custody, history separate')
s=cp(summary);s['complete_media']=False
for state,original,checkval,q in [('partial-media',None,None,inspect),('partial-media','partial-media',None,confirm),('incomplete-media-observed','unknown','incomplete-media-observed',check)]:pub(state+'-'+q['action'],q,result(state,q['action'],original,checkval,s),'accept','Explicit intentional omission')
unknown=result('unknown','confirm-export','unknown');pub('unknown-original',confirm,unknown,'accept','Possible dispatch without receipt')
pub('known-not-dispatched',confirm,result('not-dispatched','confirm-export','not-dispatched'),'accept','Only exact valid pre-export refusal')
pub('unresolved-keeps-unknown',check,result('unresolved','check-export','unknown','unresolved'),'accept','No rollback/history inference')
v=result('archive-observed','check-export','unknown','archive-observed',summary);v['selected_archive']['original_outcome']='exported';pub('check-upgrades-history-row-mismatch',check,v,'refuse','Original and matching row agree, immutable original enforced in lifecycle')
for id,mutate in [('wrong-invocation',lambda v:v['selected_archive'].update(invocation=uid(9))),('wrong-reference',lambda v:v['selected_archive'].update(reference='c'*64)),('wrong-identity',lambda v:v['observation'].update(connection_id='c'*64)),('missing-summary',lambda v:v['selected_archive'].update(summary=None)),('invented-check-exported',lambda v:v['selected_archive'].update(original_outcome='exported')),('private-path',lambda v:v['selected_archive'].update(path=path))]:
 v=result('archive-observed','check-export','unknown','archive-observed',summary);mutate(v);pub(id,check,v,'refuse','Closed phase/context/private fields')
v=cp(unknown);v['selected_archive']['summary']=cp(summary);pub('unknown-with-summary',confirm,v,'refuse','Unknown cannot carry invented custody')
v=result('exported','confirm-export','exported',None,summary);pub('check-returns-export-action',check,v,'refuse','Read-only check cannot report export execution')
v=result('idle','retained');v.update(status='unconfigured',observation=None);v['selected_archive'].update(reference=None,invocation=None,retained=[row('unknown',True)]);pub('retained-expired-safe-row',{'action':'retained'},v,'accept','Expired metadata stays bounded, no private authority')
retained_base=cp(v)
for count,expect in [(8,'accept'),(9,'refuse')]:
 v=cp(retained_base);v['selected_archive']['retained']=[{**row('unknown',True),'reference':f'{i+1:064x}'} for i in range(count)]
 pub(f'retained-{count}-distinct',{'action':'retained'},v,expect,'Independent row-capacity boundary; all references distinct and valid')
v=cp(retained_base);v['selected_archive']['retained']=[row(),row()];pub('retained-two-duplicates',{'action':'retained'},v,'refuse','Uniqueness independent of capacity: two rows only')
v=result('archive-observed','check-export','exported','archive-observed',summary)
pub('check-forged-self-consistent-upgrade',check,v,'refuse','Both result and row say exported, captured original remains unknown')
for field,value in [('connection_id','c'*64),('boot_id',uid(99))]:
 v=result('archive-observed','check-export','unknown','archive-observed',summary);v['selected_archive']['retained'][0][field]=value
 pub('check-row-wrong-'+field,check,v,'refuse','Matching reference is insufficient: captured original row identity must match')
pub('check-known-exported-history',check,result('archive-observed','check-export','exported','archive-observed',summary),'accept','Captured known history remains known without inventing it',expected_original='exported')
v=cp(unknown);v['selected_archive']['retained']=[];pub('original-without-row',confirm,v,'refuse','Every attempted original has matching retained metadata')
life=[]
def lc(id,steps,expect):life.append({'id':id,'steps':steps,'expected':expect})
lc('policy-preview-no-producer',['prepare-export(A)'],{'producer_calls':[],'summary':None,'ready_seconds':120})
lc('one-export-only',['prepare-export(A)','confirm-export(A,x)','confirm-export(A,y)'],{'export_calls':1,'second':'refuse','original_unchanged':True})
lc('unknown-then-valid-check',['confirm(A):lost-output','check(A):valid-format2'],{'original_outcome':'unknown','check_outcome':'archive-observed','export_calls':1,'publisher_proven':False})
lc('unknown-then-refused-check',['confirm(A):lost-output','check(A):unsupported'],{'original_outcome':'unknown','rollback_proven':False,'export_calls':1})
lc('late-identity',['inspect(A):pending','refresh(same-IDs)','complete(A)'],{'late_view_ignored':True,'draft_dom_empty':True})
lc('identity-change',['preview(A)','connect(B)','confirm(A)'],{'export_calls':0,'A_original_not_rebound':True})
lc('ready-expiry',['preview(A,t0)','confirm(A,t0+120s)'],{'export_calls':0,'authority_expired':True})
lc('original-nonrenewal',['confirm(A,t0):unknown','check(A,t0+29m)','check(A,t0+30m)'],{'last_dispatch':False,'private_buffers_erased':True,'safe_row_kept':True})
lc('new-with-room',['confirm(A):unknown','preview(B,same-target)','confirm(B)'],{'A_bytes_deadline_history_unchanged':True,'new_operation_distinct':True})
lc('expired-row-with-room',['A:expired-row','preview(B)'],{'A_slot_still_occupied':True,'B_may_reserve_room':True})
lc('eight-rows-full',['8retained-including-expired','preview(B)'],{'status':'capacity','producer_calls':0,'evictions':0})
lc('invocation-full',['A:32entries','check(A,new)'],{'dispatch':False,'deadline_renewed':False})
lc('cancel-before-ref',['inspect(A,x):queued','cancel(null,x)','admit(x)'],{'dispatch':False,'exact_invocation_fenced':True})
lc('cancel-stale-successor',['confirm(A,x):settled','check(A,y):owner','cancel(A,x)'],{'successor_y_untouched':True,'global_cancel_calls':0})
lc('cancel-after-export-dispatch',['confirm(A,x):possible-dispatch','cancel(A,x)'],{'original_outcome':'unknown','cleanup':False,'reexport':False})
lc('cancel-completed-export',['confirm(A):exported','cancel(A,old)'],{'original_outcome':'exported','cancel_status':'unavailable','reexport':False})
lc('corrupt-input-custody',['preview(A)','flip-original-input-byte','confirm(A)'],{'export_calls':0,'no_reconstruction':True})
lc('corrupt-retained-custody',['confirm(A):unknown','flip-path-buffer','check(A)'],{'inspect_calls':0,'original_outcome':'unknown'})
lc('busy-before-hooks',['peer-owner','prepare-export(A)'],{'hooks':0,'cancel_calls':0,'dispatch':0,'known_busy_draft_preserved':True})
lc('quiescence-queued-observation',['observation:queued','archive-admitted','observation:late'],{'late_observation_no_dispatch':True,'archive_owner_preserved':True})
lc('sensitive-boundaries',['paste-exact-CRLF','admit-before-await','pagehide-bfcache','destroy'],{'signal_empty':True,'actual_DOM_empty':True,'no_url_log_persistence':True})
lc('check-not-same-publisher',['confirm(A):unknown','external-valid-archive-at-original-path','check(A):ok'],{'original_outcome':'unknown','publisher_proven':False})
lc('gen3-vs-pending4',['inspect:format3-ok','export-selected:unsupported-feedback3','future-format4-report'],{'inspect3_admitted':True,'export_no_fallback':True,'format4_refused':True})
lc('read-inspect-not-original',['inspect(A):ok','inspect(B):ok'],{'export_rows_allocated':0,'private_paths_dropped':True})
lc('known-reference-cancel-remains-fenced',['original(A):retained','cancel(A,check-x):before-arrival','15seconds-pass','check(A,x)'],{'inspect_dispatch':False,'original_history_unchanged':True,'fence_in_original_ledger':True,'session_fence_expiry_not_new_authority':True})
v={'schema':1,'purpose':'Independent literal proposed admission and lifecycle oracles, no implementation/producer replay','context':{'connection_id':cid,'boot_id':boot,'reference':ref,'invocation':inv,'path':path,'summary':summary},'raw_cases':raw,'request_cases':request,'public_cases':public,'lifecycle_cases':life}
(p/'vectors.json').write_text(json.dumps(v,indent=2,ensure_ascii=True)+'\n')
print({k:len(v[k]) for k in ['raw_cases','request_cases','public_cases','lifecycle_cases']})
