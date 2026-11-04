"""Independent fixture-integrity checks only, never a consumer/producer test."""
from pathlib import Path
import hashlib,json
p=Path(__file__).resolve().parent;v=json.loads((p/'vectors.json').read_text());groups=['raw_cases','request_cases','packet_cases','public_cases','lifecycle_cases'];ids=[c['id'] for g in groups for c in v[g]]
assert len(ids)==len(set(ids))
for c in v['raw_cases']:
 b=c['stdout_utf8'].encode();assert len(b)==c['stdout_bytes'];assert hashlib.sha256(b).hexdigest()==c['stdout_sha256']
i=v['context']['intent'];assert len(i)==14;assert i['base_generation']!=i['target_generation']
for key,domain,path in [('config_path_sha256','config',v['context']['config']),('source_path_sha256','source',v['context']['source'])]:assert i[key]==hashlib.sha256(('urn:remarkable-buddies:ordinary-restore-'+domain+'-path:v1:'+path).encode()).hexdigest()
c=v['packet_cases'][0];assert len(c['prepare_utf8'].encode())==c['prepare_bytes']<=16384<c['original_bytes']==len(c['original_utf8'].encode())
r={c['id']:c for c in v['request_cases']};assert r['prepare-valid']['request']['invocation']!=r['confirm-fresh-invocation']['request']['invocation']!=r['status-fresh-invocation']['request']['invocation']
assert r['cancel-target-ready-creator']['request']['invocation']==r['prepare-valid']['request']['invocation']
assert r['cancel-target-active-confirm']['request']['invocation']==r['confirm-fresh-invocation']['request']['invocation']
result={'vector_artifact':'vectors.json','unique_cases':len(ids),**{g:len(v[g]) for g in groups},'checks':'JSON syntax, unique IDs, raw lengths/digests, fourteen-field fixture, distinct original path domains, packet overflow and explicit executing-versus-targeted-cancel invocation relationships','not_tested':'No consumer parser exists yet. Literal accept/reject/lifecycle expectations are proposed oracles, not implementation passes. No producer/device replay.','previous_independent_history_check':{'history_sha256':'8df8ee19ccf766193ae7d6064bb62c724a66268fb0a904e6b2d34f3e1d904b94','limit':'Synthetic serialization only; object contents and lineage not qualified; exact supplied source/golden vector originally hash-verified as pinned in source-proof.json.'}}
(p/'vector-integrity.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
