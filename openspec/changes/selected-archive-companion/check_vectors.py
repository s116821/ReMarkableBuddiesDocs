"""Fixture integrity only. Never a consumer parser, producer replay or host test."""
from pathlib import Path
import hashlib,json
p=Path(__file__).resolve().parent
v=json.loads((p/'vectors.json').read_text());groups=['raw_cases','request_cases','public_cases','lifecycle_cases']
ids=[c['id'] for g in groups for c in v[g]];assert len(ids)==len(set(ids))
for c in v['raw_cases']:
 b=bytes.fromhex(c['stdout_hex']) if 'stdout_hex' in c else c['stdout_utf8'].encode()
 assert len(b)==c['stdout_bytes'];assert hashlib.sha256(b).hexdigest()==c['stdout_sha256']
 assert c['expect'] in ['accept','refuse']
r={c['id']:c for c in v['raw_cases']};assert r['report-bytes-16384']['stdout_bytes']==16384 and r['report-bytes-16385']['stdout_bytes']==16385
q={c['id']:c for c in v['request_cases']};assert len(q['path-exact']['request']['path'].encode())==4096
assert q['cancel-exact-target']['request']['invocation']==v['context']['invocation']
assert q['cancel-before-reference']['request']['reference'] is None
assert q['path-opaque-crlf']['request']['path']=='/a\r\n '
public={c['id']:c for c in v['public_cases']}
assert public['ready-policy-only']['result']['selected_archive']['summary'] is None
assert public['archive-observed-valid']['result']['selected_archive']['original_outcome']=='unknown'
for name,count,distinct,expect in [('retained-8-distinct',8,8,'accept'),('retained-9-distinct',9,9,'refuse'),('retained-two-duplicates',2,1,'refuse')]:
 c=public[name];rows=c['result']['selected_archive']['retained'];assert len(rows)==count and len({r['reference'] for r in rows})==distinct and c['expect']==expect
c=public['check-forged-self-consistent-upgrade'];assert c['response_context']['expected_original_outcome']=='unknown' and c['result']['selected_archive']['original_outcome']=='exported' and c['result']['selected_archive']['retained'][0]['original_outcome']=='exported' and c['expect']=='refuse'
for field in ['connection_id','boot_id']:
 c=public['check-row-wrong-'+field];r=c['result']['selected_archive']['retained'][0];assert r['reference']==c['response_context']['reference'] and r[field]!=c['response_context'][field] and c['expect']=='refuse'
for c in v['public_cases']:
 if c['request']['action']=='check-export':assert 'expected_original_outcome' in c['response_context'] and 'expected_original_outcome' not in c['request']
assert q['renderer-cannot-supply-expected-history']['expect']=='refuse'
result={'total_cases':len(ids),**{g:len(v[g]) for g in groups},'vectors_sha256':hashlib.sha256((p/'vectors.json').read_bytes()).hexdigest(),'checks':'Unique IDs; raw bytes/digests; inclusive report/path boundaries; target-invocation cancellation; literal CRLF preservation; independent8/9unique/two-duplicate boundaries; private captured-history/self-consistent-upgrade and wrong-row-identity fixture integrity.','not_tested':'No consumer implementation or producer replay. Expect fields are proposed independent oracles. No device/provider/native/host execution.'}
(p/'vector-integrity.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
