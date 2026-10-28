"""Specification fixture authoring only; does not run a consumer or producer."""
from pathlib import Path
import base64,copy,hashlib,json
P=Path(__file__).resolve().parent
compact=lambda v:json.dumps(v,separators=(',',':'),ensure_ascii=False)
hash=lambda s:hashlib.sha256(s.encode()).hexdigest()
clone=copy.deepcopy
config='/home/root/.config/remarkable-buddies/config.json';source='/home/root/backups/ordinary-archive'
u=lambda n:f'{n*8}-{n*4}-4{n*3}-8{n*3}-{n*12}'
operation=u('1');actor=u('2');base=u('3');target=u('4');inv=u('6');boot=u('7');reference='b'*64
identity={'connection_id':'a'*64,'boot_id':boot}
intent={'restore_version':1,'operation':operation,'config_path_sha256':hash('urn:remarkable-buddies:ordinary-restore-config-path:v1:'+config),'config_sha256':'1'*64,'source_path_sha256':hash('urn:remarkable-buddies:ordinary-restore-source-path:v1:'+source),'archive_sha256':'2'*64,'actor':actor,'mode_sha256':'3'*64,'base_generation':base,'base_history_sha256':'4'*64,'target_generation':target,'target_history_sha256':'5'*64,'staged_configuration_sha256':'6'*64,'complete_media':False}
summary=lambda n,o,media,conf:{'manifests':n,'objects':o,'complete_media':media,'configuration_included':conf}
preview={'source':summary(2,4,True,True),'target':summary(5,9,False,True),'additional_manifests':1,'additive':True,'configuration_applied':False}
context={'operation':operation,'source':source,'config':config,'intent':intent,'preview':preview}
report=lambda op,status,outcome,readback=False,data=None:{'report_version':1,'operation':op,'status':status,'outcome':outcome,'disk_readback_verified':readback,'runtime_activation':'unverified','data':data}
prepared=report('prepare','ok','prepared',data={'preview':preview,'intent':intent})
restored=report('apply','ok','restored',True,{'inspection':preview['target'],'configuration_applied':False})
desired=report('status','ok','desired-generation-observed',False,{'inspection':preview['target'],'configuration_applied':False})
raw=[]
def add(name,op,value,expect,why,ctx=None):
 s=value if isinstance(value,str) else compact(value)+'\n'
 raw.append({'id':name,'selector':op,'stdout_utf8':s,'stdout_bytes':len(s.encode()),'stdout_sha256':hash(s),'context':clone(ctx or context),'expect':expect,'basis':why})
add('prepared-valid-target-media-differs-from-source','prepare',prepared,'accept','union completeness need not equal source flag')
noConfig=clone(prepared);noConfig['data']['intent']['staged_configuration_sha256']=None
for side in ['source','target']:noConfig['data']['preview'][side]['configuration_included']=False
add('prepared-valid-no-inactive-config','prepare',noConfig,'accept','required nullable remains explicit')
add('restored-exact-target','apply',restored,'accept','only Apply success has true disk readback')
add('desired-exact-target-not-receipt','status',desired,'accept','read-only desired closure not original publication identity')
add('unresolved-original','status',report('status','ok','unresolved'),'accept','no data or historical settlement')
for op in ['prepare','apply','status']:
 for status in ['invalid-input','unavailable','unsupported','busy','conflict','failed']:
  add(f'{op}-{status}-not-dispatched',op,report(op,status,'not-dispatched'),'accept','refusal concerns only current invocation; Status cannot settle earlier Apply')
for outcome in ['not-activated','unknown']:
 add('apply-failed-'+outcome,'apply',report('apply','failed',outcome),'accept','preserve phase evidence and original custody')
negatives=[('wrong-selector','status',restored,'phase mismatch'),('status-success-readback-true','status',{**desired,'disk_readback_verified':True},'Status never verified original Apply readback'),('apply-success-readback-false','apply',{**restored,'disk_readback_verified':False},'Apply success requires readback'),('runtime-verified','apply',{**restored,'runtime_activation':'verified'},'runtime remains unverified'),('status-not-activated','status',report('status','failed','not-activated'),'only Apply may report staged publication phase'),('prepare-unknown','prepare',report('prepare','failed','unknown'),'Prepare cannot publish'),('status-unknown','status',report('status','failed','unknown'),'producer Status has no unknown outcome'),('apply-ok-unknown','apply',report('apply','ok','unknown'),'unknown requires failed status'),('unresolved-has-data','status',report('status','ok','unresolved',data={'inspection':preview['target'],'configuration_applied':False}),'unresolved data null'),('refusal-has-data','apply',report('apply','busy','not-dispatched',data={}), 'refusal data null'),('unknown-readback','apply',report('apply','failed','unknown',True),'unknown readback false'),('raw-extra-key','apply',{**restored,'source':source},'no extra raw keys'),('version-array','apply',{**restored,'report_version':[]},'version exact scalar')]
for name,op,value,why in negatives:add(name,op,value,'reject',why)
add('positive-future-version','prepare',{**prepared,'report_version':2},'unsupported','future supported-shape version is not current admission')
def mutate(name,changes,why):
 v=clone(prepared);changes(v);add(name,'prepare',v,'reject',why)
mutate('wrong-operation-context',lambda x:x['data']['intent'].__setitem__('operation',u('9')),'host operation binding')
mutate('wrong-source-domain',lambda x:x['data']['intent'].__setitem__('source_path_sha256',hash('urn:remarkable-buddies:ordinary-restore-config-path:v1:'+source)),'source/config domains distinct')
mutate('wrong-config-domain',lambda x:x['data']['intent'].__setitem__('config_path_sha256',hash(config)),'bare path hash is wrong')
mutate('wrong-export-source-domain',lambda x:x['data']['intent'].__setitem__('source_path_sha256',hash('urn:remarkable-buddies:ordinary-export-path:v1:'+source)),'export domain is not restore domain')
mutate('base-equals-target',lambda x:x['data']['intent'].__setitem__('target_generation',base),'fresh desired generation')
mutate('missing-nullable',lambda x:x['data']['intent'].pop('staged_configuration_sha256'),'exact fourteen fields even null')
mutate('invented-intent-self-hash',lambda x:x['data']['intent'].__setitem__('intent_sha256','0'*64),'producer intent has no self-digest')
mutate('config-presence-disagrees',lambda x:x['data']['intent'].__setitem__('staged_configuration_sha256',None),'null iff source/target configuration absent')
mutate('target-media-disagrees',lambda x:x['data']['intent'].__setitem__('complete_media',True),'intent binds target media flag')
mutate('target-count-overbound',lambda x:x['data']['preview']['target'].__setitem__('objects',4097),'union count cap')
mutate('additional-over-source',lambda x:x['data']['preview'].__setitem__('additional_manifests',3),'additional at most source and target')
mutate('source-target-config-disagree',lambda x:x['data']['preview']['target'].__setitem__('configuration_included',False),'target inactive config originates in archive')
mutate('unexpected-format-field',lambda x:x['data']['preview']['source'].__setitem__('format',1),'restore SUMMARY has four fields, unlike export')
wrong=clone(restored);wrong['data']['inspection']['objects']=8;add('apply-wrong-original-inspection','apply',wrong,'reject','exact original target summary')
wrong=clone(desired);wrong['data']['configuration_applied']=True;add('status-active-config-claim','status',wrong,'reject','configuration never activated')
for name,s in [('duplicate-header',compact(prepared).replace('"report_version":1','"report_version":1,"report_version":1',1)+'\n'),('missing-terminal-lf',compact(prepared)),('two-terminal-lfs',compact(prepared)+'\n\n'),('trailing-json',compact(prepared)+'{}\n'),('bom','\ufeff'+compact(prepared)+'\n'),('top-array','[]\n')]:add(name,'prepare',s,'reject','strict original framing/shape')
requests=[]
def req(name,q,expect,why):requests.append({'id':name,'request':clone(q),'expect':expect,'basis':why})
pq={'action':'prepare',**identity,'invocation':inv,'source':source};cq={'action':'confirm',**identity,'invocation':u('8'),'reference':reference}
req('prepare-valid',pq,'accept','only entry for untrusted source draft')
req('confirm-fresh-invocation',cq,'accept','executing Confirm has a fresh invocation distinct from Prepare creator')
req('status-fresh-invocation',{**cq,'action':'status','invocation':u('9')},'accept','executing Status has a fresh invocation')
req('cancel-target-active-confirm',{**cq,'action':'cancel'},'accept','Cancel names existing Confirm invocation, not a fresh cancellation action')
req('cancel-target-ready-creator',{**cq,'action':'cancel','invocation':inv},'accept','Cancel names Prepare creator when canceling idle ready grant')
req('retained-valid',{'action':'retained'},'accept','host memory only')
for action in ['confirm','status','cancel']:req(action+'-source-injection',{**cq,'action':action,'source':source},'reject','source prohibited outside Prepare')
for key in ['intent','operation','target_generation','config','budget_ms']:req('prepare-extra-'+key,{**pq,key:{} if key=='intent' else target},'reject','exact request and no renderer authority')
for name,path in [('relative','backups/archive'),('root','/'),('parent','/backups/../archive'),('dot','/backups/./archive'),('trailing-slash','/backups/archive/'),('nul','/backups/\x00archive'),('unpaired-surrogate','/backups/\ud800'),('over-utf8','/'+'é'*2048)]:req('path-'+name,{**pq,'source':path},'reject','proposed strict scalar/POSIX path subset and4096UTF8 bound')
req('path-unicode-valid',{**pq,'source':'/home/root/backups/café archive'},'accept','exact scalar UTF8, no trimming')
req('cancel-wrong-identity-shape',{**cq,'action':'cancel','boot_id':'0'*36},'reject','Cancel includes valid captured identity')
# Boundary bytes are concrete fixtures, never an expectation derived by the future parser.
bigSource='/'+'\x01'*2630
bigI=clone(intent);bigI['source_path_sha256']=hash('urn:remarkable-buddies:ordinary-restore-source-path:v1:'+bigSource)
preparePacket={'restore_version':1,'operation':operation,'source':bigSource};originalPacket={'source':bigSource,'intent':bigI}
assert len(compact(preparePacket).encode())<=16384 < len(compact(originalPacket).encode())
packet_case={'id':'prepare-fits-but-original-does-not','source':bigSource,'source_utf8_bytes':len(bigSource.encode()),'prepare_utf8':compact(preparePacket),'prepare_bytes':len(compact(preparePacket).encode()),'original_utf8':compact(originalPacket),'original_bytes':len(compact(originalPacket).encode()),'expect':'refuse-ready','basis':'bound original Apply and Status before granting ready; no truncation'}
obs={'model':'reMarkable 1','firmware':'3.0.0','firmware_conflict':False,'architecture':'armv7l',**identity,'service':{'LoadState':'loaded','ActiveState':'inactive','SubState':'dead'},'installed_version':None,'provenance':'unknown'}
row=lambda state='unknown',outcome='unknown':{'reference':reference,**identity,'state':state,'apply_outcome':outcome,'status_available':True}
reduce=lambda r:{k:r[k] for k in ['operation','status','outcome','disk_readback_verified','runtime_activation']}
def public(state,rawReport=None,previewValue=None,inspection=None,outcome=None,rows=None,local=False):return {'contract_version':1,'status':'unconfigured' if local else 'observed','observation':None if local else obs,'ordinary_restore':{'state':state,'reference':None if state in ['ready-new-refused','none','busy-local'] else reference,'preview':previewValue,'inspection':inspection,'report':None if rawReport is None else reduce(rawReport),'apply_outcome':outcome,'retained':rows or []}}
publics=[]
def pub(name,q,result,expect,why):publics.append({'id':name,'request':clone(q),'result':clone(result),'expect':expect,'basis':why})
ready=public('ready',prepared,preview);verified=public('restored',restored,inspection=preview['target'],outcome='restored');d=public('desired-generation-observed',desired,inspection=preview['target'],outcome='unknown')
pub('ready-valid',pq,ready,'accept','fresh observed preview only')
pub('restored-valid',cq,verified,'accept','original Apply exact disk readback')
sq={**cq,'action':'status','invocation':u('9')};pub('desired-keeps-unknown-history',sq,d,'accept','no historical publisher proof')
dn=clone(d);dn['ordinary_restore']['apply_outcome']='not-activated';pub('desired-keeps-not-activated-history',sq,dn,'accept','current state can be observed without original CURRENT attempt')
unresolved=public('unresolved',report('status','ok','unresolved'),outcome='unknown',rows=[row('unresolved')]);pub('unresolved-valid',sq,unresolved,'accept','prior Apply uncertainty remains')
unknown=public('unknown',outcome='unknown',rows=[row()],local=True);pub('apply-lost-output',cq,unknown,'accept','loss after possible dispatch retains original')
na=public('not-activated',report('apply','failed','not-activated'),outcome='not-activated',rows=[row('not-activated','not-activated')]);pub('not-activated-retains-staging-evidence',cq,na,'accept','no CURRENT attempt, possible staged files')
busy=public('busy',local=True);busy['ordinary_restore']['reference']=None;pub('prepare-local-busy',pq,busy,'accept','no new reference or report')
r=public('none',local=True);r['ordinary_restore']['retained']=[row()];pub('retained-memory',{'action':'retained'},r,'accept','no target observation')
for name,value,request,why in [('wrong-selected-identity',unknown,cq,'selected row must match captured request'),('unknown-no-row',unknown,cq,'original cannot vanish on lost reply'),('ready-with-inspection',ready,pq,'preview and terminal inspection separate'),('status-promotes-history',d,sq,'Status never sets original Apply restored'),('desired-keeps-selected-row',d,sq,'terminal desired retires selected custody after safe result'),('report-without-observation',na,cq,'admitted raw report needs observed requested identity'),('status-uses-apply-report',verified,sq,'phase and action independently checked')]:
 v=clone(value);w=v['ordinary_restore']
 if name=='wrong-selected-identity':w['retained'][0]['boot_id']=u('8')
 if name=='unknown-no-row':w['retained']=[]
 if name=='ready-with-inspection':w['inspection']=preview['target']
 if name=='status-promotes-history':w['apply_outcome']='restored'
 if name=='desired-keeps-selected-row':w['retained']=[row()]
 if name=='report-without-observation':v['status']='unconfigured';v['observation']=None
 pub(name,request,v,'reject',why)
# Positive unrelated retained rows do not force identity equality with every row.
v=clone(unknown);other=row();other['reference']='c'*64;other['boot_id']=u('8');v['ordinary_restore']['retained'].append(other);pub('unrelated-original-identity-allowed',cq,v,'accept','only selected retained row binds this request')
lifecycle=[
 {'id':'lost-apply-status-unresolved','events':['ready','Confirm admitted','Apply output lost','Status ok/unresolved'],'expected':{'apply_calls':1,'status_calls':1,'retained':True,'apply_outcome':'unknown','ready':False}},
 {'id':'not-activated-status-refused','events':['ready','Apply failed/not-activated','Status conflict/not-dispatched'],'expected':{'apply_calls':1,'retained':True,'apply_outcome':'not-activated','stage_cleanup_calls':0}},
 {'id':'unknown-desired-observation','events':['Apply lost','Status ok/desired-generation-observed'],'expected':{'apply_calls':1,'retained':False,'apply_outcome':'unknown','historical_acknowledgment':False}},
 {'id':'cancel-old-invocation','events':['Status invocation A finishes','Status invocation B starts','delayed Cancel A'],'expected':{'B_cancelled':False,'B_owner_released_by_A':False}},
 {'id':'late-original-expiry','events':['Apply unknown deadline T','Status refused at T-1','custody expires T'],'expected':{'deadline_renewed':False,'status_available':False,'safe_row_preserved':True}},
 {'id':'host-busy-before-hooks','events':['other owner active','Prepare submitted'],'expected':{'hooks':0,'helper_calls':0,'peer_invalidations':0,'new_grants':0}},
 {'id':'ready-to-confirm-once','events':['ready','Confirm','duplicate Confirm same invocation','Confirm fresh invocation'],'expected':{'apply_calls':1,'ready_consumed':True}},
 {'id':'custody-packet-mutated','events':['ready','stored packet byte mutated','Confirm'],'expected':{'apply_calls':0,'state':'not-dispatched','no_reconstruction':True}},
 {'id':'original-report-mutated','events':['ready','stored prepared report hash differs','Confirm'],'expected':{'apply_calls':0,'state':'not-dispatched','no_reprepare':True}},
 {'id':'prepare-lifetime-source-erasure','events':['private source signal and textarea populated','Prepare admission before first await','pagehide persisted'],'expected':{'signal':'','textarea_value':'','path_in_safe_response':False,'path_in_storage_or_logs':False}},
 {'id':'genuine-original-busy-refusal','events':['genuine original unknown','new action Busy/capacity'],'expected':{'genuine_row_preserved':True,'deadline_renewed':False,'new_speculative_rows':0}},
 {'id':'new-same-target-with-room','before':{'retained_rows':1,'active_action':None,'owner':'free','old_reference':reference,'old_apply_outcome':'unknown','old_original_sha256':hash(compact({'source':source,'intent':intent})),'old_deadline':1800000,'old_ledger':[inv,u('8')]},'events':['new deliberate Prepare same target and path with fresh invocation','new preview','new deliberate Confirm'],'expected':{'producer_prepare_calls':1,'new_operation_differs':True,'new_reference_differs':True,'old_bytes_hash_identity_deadline_ledger_row_unchanged':True,'old_apply_outcome':'unknown','automatic_apply_calls':0}},
 {'id':'new-distinct-identity-with-room','before':{'retained_rows':1,'active_action':None,'owner':'free','old_identity':identity},'new_identity':{'connection_id':'c'*64,'boot_id':u('9')},'events':['explicitly observed different identity','new deliberate Prepare'],'expected':{'producer_prepare_calls':1,'new_operation_differs':True,'new_reference_differs':True,'old_captured_identity_unchanged':True,'old_private_custody_unchanged':True}},
 {'id':'expired-row-with-room','before':{'retained_rows':1,'expired_rows':1,'active_action':None,'owner':'free'},'events':['new deliberate Prepare'],'expected':{'producer_prepare_calls':1,'expired_row_preserved':True,'expired_status_available':False,'new_reference_differs':True,'old_deadline_not_renewed':True}},
 {'id':'full-capacity-with-expired-row','before':{'retained_rows':8,'expired_rows':1,'active_action':None,'owner':'free'},'events':['new deliberate Prepare'],'expected':{'producer_prepare_calls':0,'state':'capacity','evicted_rows':0,'old_bytes_hash_identity_deadlines_ledgers_rows_unchanged':True}},
 {'id':'new-prepare-active-prior-action','before':{'retained_rows':1,'owner':'ordinary-restore','active_action':'status-A'},'events':['new Prepare B while A active'],'expected':{'B_producer_prepare_calls':0,'state':'busy','A_cancelled':False,'A_deadline_unchanged':True,'new_grants':0}},
 {'id':'old-status-after-later-restore','events':['old Apply unknown','new deliberate restore accepted and confirmed under fresh original','explicit old Status ok/unresolved'],'expected':{'old_packet_unchanged':True,'old_apply_outcome':'unknown','old_deadline_unchanged':True,'old_historical_rollback_proven':False,'old_status_retries_apply':False}},
 {'id':'cancel-active-confirm-exact-invocation','before':{'reference':reference,'creator_invocation':inv,'active_invocation':u('8'),'active_action':'confirm','possible_dispatch':True},'cancel':{'action':'cancel',**identity,'reference':reference,'invocation':u('8')},'expected':{'only_active_confirm_cancelled':True,'apply_outcome':'unknown','original_retained':True,'apply_replayed':False}},
 {'id':'cancel-idle-ready-creator','before':{'reference':reference,'creator_invocation':inv,'active_action':None,'state':'ready'},'cancel':{'action':'cancel',**identity,'reference':reference,'invocation':inv},'expected':{'ready_invalidated':True,'apply_calls':0,'new_cancel_invocation_allocated':False}},
 {'id':'cancel-unrelated-uuid-cannot-revoke-ready','before':{'reference':reference,'creator_invocation':inv,'active_action':None,'state':'ready'},'cancel':{'action':'cancel',**identity,'reference':reference,'invocation':u('5')},'expected':{'ready_invalidated':False,'producer_calls':0,'owner_released':False}},
 {'id':'cancel-before-status-request-fenced','events':['Cancel target reference + identity + invocation A arrives first','Status executing invocation A arrives','Status fresh invocation B arrives after fence settled'],'expected':{'A_status_dispatches':0,'B_status_dispatches':1,'fence_bounded_by_ledger':True,'B_cancelled_by_A':False}},
 {'id':'cancel-repeated-while-successor-active','events':['Status A canceled','Status B starts same reference with fresh invocation','repeat Cancel A twice'],'expected':{'B_cancelled':False,'B_owner_released':False,'extra_producer_calls':0,'unbounded_cancel_ledger_growth':False}}]
fixture={'fixture_version':1,'status':'precode literal expectations only; no consumer/producer execution or implementation pass','basis':'contract.md candidate + exact supplied producer source; original corpus attribution in source-proof.json','context':context,'raw_cases':raw,'request_cases':requests,'packet_cases':[packet_case],'public_cases':publics,'lifecycle_cases':lifecycle}
(P/'vectors.json').write_text(json.dumps(fixture,indent=2,ensure_ascii=True)+'\n')
print(json.dumps({'raw':len(raw),'requests':len(requests),'packet':1,'public':len(publics),'lifecycle':len(lifecycle),'prepare_boundary_bytes':packet_case['prepare_bytes'],'original_boundary_bytes':packet_case['original_bytes']}))
