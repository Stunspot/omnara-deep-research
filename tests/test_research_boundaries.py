"""Declared review fixtures are fictional; no simulated case is a model trial."""
import copy,json,shutil,sys,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
R=Path(__file__).parents[1];sys.path[:0]=[str(R/'scripts'),str(R/'workspace')]
import research_campaign as native
from evidence_contract import subject,review_status,clock,loads
from citation_audit import audit
from assemble_report import assemble
from campaign import CampaignRoom
import campaign

def write(p,value):p.write_text(json.dumps(value,indent=2)+'\n',encoding='utf-8',newline='\n')
def ledger(p,rows):p.write_text(''.join(json.dumps(x)+'\n' for x in rows),encoding='utf-8',newline='\n')
def seed(path):
    native.initialize(R/'assets/campaign-vault',path,'Pump measurement fixture','Does a lower gauge reading establish lower water volume?','focused')
    source={'id':'S001','title':'Fictional gauge observation','identifier':'fixture:gauge','states':['discovered','inspected','opened','deeply-read','cited'],'published_at':'2026-09-01','accessed_at':'2026-10-06'}
    ledger(path/'source-ledger.jsonl',[source]);ledger(path/'claim-ledger.jsonl',[{'id':'C001','claim':'The recorded level is lower; the volume inference remains unestablished.','source_ids':['S001'],'semantic_audit':'supported'}])
    (path/'notes/S001.md').write_text('# Fictional source\n\nThe gauge reports a lower level at its new location. The tank geometry and reference point changed. This observation does not isolate water volume; original geometry and common datum are required. This is an authored test fixture, not field evidence.\n',encoding='utf-8')
    texts={'research-brief.md':'Determine whether a changed gauge level establishes changed volume. Compare fixed geometry and common datum; preserve uncertainty.','coverage-matrix.md':'Level is recorded. Tank geometry and reference datum are missing. Volume is not established.','contradictions.md':'No contradictory measurement was supplied; the missing geometry prevents a like-for-like inference.','campaign-summary.md':'One fictional source describes level. No claim of volume loss is justified. Reopen on common-datum measurements and tank geometry.','report.md':'# Gauge and volume\n\nThe recorded level is lower; the volume inference remains unestablished. [S001]\n\n## Sources\n\n[S001] Fictional gauge observation — fixture:gauge\n'}
    for name,value in texts.items():(path/name).write_text(value+'\n',encoding='utf-8',newline='\n')
    c=native.read_json(path/'campaign.json');c['counters'].update({s.replace('-','_'):1 for s in source['states']});c.update(phase='review',status='active',evidence_cutoff='2026-09-30');write(path/'campaign.json',c)
    seal(path);return path

def seal(path):
    # Explicitly fictional current attestations isolate each mechanical boundary.
    write(path/'citation-audit-structural.json',audit(path))
    review={'format':'omnara-semantic-review/v1','subject_sha256':subject(path)['sha256'],'reviewer':'fictional fixture reviewer','reviewed_at':'2026-10-06','result':'pass','rationale':'Fictional test attestation: lower level does not establish lower volume after datum and geometry change.','claims':[{'claim_id':r['id'],'treatment':'qualified','rationale':'The report explicitly limits the inference to the observed metric.'} for r in native.read_jsonl(path/'claim-ledger.jsonl')]};write(path/'semantic-review.json',review)

def complete(path):
    c=native.read_json(path/'campaign.json');c.update(phase='complete',status='complete');write(path/'campaign.json',c)

class EvidenceTests(unittest.TestCase):
    def setUp(self):self.t=tempfile.TemporaryDirectory();self.addCleanup(self.t.cleanup);self.p=seed(Path(self.t.name)/'case')
    def errors(self):return '\n'.join(native.validate(self.p))
    def test_complete_positive(self):complete(self.p);self.assertEqual(native.validate(self.p),[])
    def test_status_only_not_complete(self):
        c=native.read_json(self.p/'campaign.json');c['status']='complete';write(self.p/'campaign.json',c);self.assertIn('must agree',self.errors())
    def test_complete_without_semantic_review(self):(self.p/'semantic-review.json').unlink();complete(self.p);self.assertIn('semantic review',self.errors())
    def test_changed_note_stales_review(self):
        (self.p/'notes/S001.md').write_text('The gauge now measures a different phenomenon.');complete(self.p);self.assertIn('stale',self.errors())
    def test_changed_scope_stales_review(self):
        (self.p/'research-brief.md').write_text('Now establish causal water loss.');complete(self.p);self.assertIn('stale',self.errors())
    def test_changed_unmarked_report_stales_review(self):
        with (self.p/'report.md').open('a',encoding='utf-8') as f:f.write('\nAll the water was stolen.\n')
        complete(self.p);self.assertIn('stale',self.errors())
    def test_admin_phase_transition_preserves_review(self):complete(self.p);self.assertEqual(review_status(self.p)['state'],'current')
    def test_missing_reviewed_claim(self):
        v=native.read_json(self.p/'semantic-review.json');v['claims']=[];write(self.p/'semantic-review.json',v);complete(self.p);self.assertIn('every recorded claim',self.errors())
    def test_unresolved_review_cannot_pass(self):
        v=native.read_json(self.p/'semantic-review.json');v['claims'][0]['treatment']='unresolved';write(self.p/'semantic-review.json',v);complete(self.p);self.assertIn('unresolved',self.errors())
    def test_citation_integrity_recomputed_not_trusted(self):
        (self.p/'report.md').write_text('# Answer\n\nUnsupported [S099]\n');seal(self.p);v=native.read_json(self.p/'citation-audit-structural.json');v.update(result='pass',errors=[]);write(self.p/'citation-audit-structural.json',v);complete(self.p);self.assertIn('no source',self.errors())
    def test_hidden_bibliography_fails_with_fresh_bindings(self):
        p=self.p/'report.md';p.write_text(p.read_text().replace('## Sources','## Sources\n<!--'));seal(self.p);complete(self.p);self.assertIn('visible Sources entry',self.errors())
    def test_literal_comment_inside_fence_preserves_bibliography(self):
        p=self.p/'report.md';p.write_text('```html\n<!-- example\n```\n'+p.read_text());seal(self.p);complete(self.p);self.assertEqual(native.validate(self.p),[])
    def test_excluded_after_reading_preserves_history(self):
        rows=native.read_jsonl(self.p/'source-ledger.jsonl');rows[0]['states'].remove('cited');rows[0]['states'].append('excluded');rows[0]['disposition']='Excluded after full reading: mismatched gauge.';ledger(self.p/'source-ledger.jsonl',rows);c=native.read_json(self.p/'campaign.json');c['counters'].update(cited=0,excluded=1);write(self.p/'campaign.json',c);self.assertEqual(native.validate(self.p),[])
    def test_duplicate_needs_canonical_record(self):
        rows=native.read_jsonl(self.p/'source-ledger.jsonl');rows.append({'id':'S002','title':'Mirror','identifier':'fixture:mirror','states':['discovered','duplicate'],'disposition':'Same original','duplicate_of':'S999'});ledger(self.p/'source-ledger.jsonl',rows);self.assertIn('duplicate_of',self.errors())
    def test_malformed_types_controlled(self):
        c=native.read_json(self.p/'campaign.json');c.update(canonical_inquiry=42,resume_point={},title=[],budgets=[]);write(self.p/'campaign.json',c);self.assertIn('substantive text',self.errors())
    def test_duplicate_json_keys(self):
        with self.assertRaisesRegex(ValueError,'duplicate JSON'):loads('{"title":"x","title":"y"}')
    def test_impossible_offset(self):
        self.assertIsNone(clock('2026-10-06T01:00:00-05:99'));self.assertIsNone(clock('2026-10-06T01:00:00'));self.assertIsNotNone(clock('2026-10-06T01:00:00+05:30'))
    def test_later_retrieval_allowed_historical_cutoff(self):self.assertEqual(native.validate(self.p),[])
    def test_later_publication_rejected(self):
        rows=native.read_jsonl(self.p/'source-ledger.jsonl');rows[0]['published_at']='2026-10-01';ledger(self.p/'source-ledger.jsonl',rows);self.assertIn('beyond declared evidence cutoff',self.errors())
    def test_zero_source_honest_result(self):
        ledger(self.p/'source-ledger.jsonl',[]);ledger(self.p/'claim-ledger.jsonl',[]);(self.p/'report.md').write_text('# Evidence unavailable\n\nNo source was supplied. This is not evidence of no water loss. A common datum and tank geometry are required.');c=native.read_json(self.p/'campaign.json');c['counters']={s.replace('-','_'):0 for s in native.SOURCE_STATES};c['counters']['queries']=0;write(self.p/'campaign.json',c);seal(self.p);complete(self.p);self.assertEqual(native.validate(self.p),[])
    def test_readonly_subject_does_not_issue_review(self):
        before={p.relative_to(self.p):p.read_bytes() for p in self.p.rglob('*') if p.is_file()};subject(self.p);self.assertEqual(before,{p.relative_to(self.p):p.read_bytes() for p in self.p.rglob('*') if p.is_file()})
    def test_assembly_preserves_report_until_authorized(self):
        (self.p/'draft/01-new.md').write_text('# New draft\nEvidence changed.');before=(self.p/'report.md').read_bytes()
        with self.assertRaisesRegex(ValueError,'--replace'):assemble(self.p)
        self.assertEqual((self.p/'report.md').read_bytes(),before);result=assemble(self.p,True);self.assertEqual(Path(result['prior_report']).read_bytes(),before);self.assertEqual(review_status(self.p)['state'],'not-current')

class RoomBoundaryTests(unittest.TestCase):
    def setUp(self):self.t=tempfile.TemporaryDirectory();self.addCleanup(self.t.cleanup);self.root=Path(self.t.name);self.room=CampaignRoom(self.root);self.v=self.room.request('POST','/api/create',{'title':'Actual user question','question':'Which fact changes this decision?'})
    def test_damaged_campaign_remains_findable_and_editable(self):
        p=self.room.directory(self.v['key']);(p/'campaign.json').write_text('{bad');rows=self.room.request('POST','/api/list',{})['campaigns'];self.assertEqual(rows[0]['status'],'damaged');loaded=self.room.load(self.v['key']);self.assertEqual(loaded['files']['campaign.json'],'{bad');self.assertTrue(loaded['validation'])
    def test_typed_corrupt_campaign_does_not_break_library(self):
        p=self.room.directory(self.v['key']);c=native.read_json(p/'campaign.json');c['updated_at']=['bad sort value'];write(p/'campaign.json',c)
        rows=self.room.request('POST','/api/list',{})['campaigns'];self.assertEqual(rows[0]['status'],'damaged');self.assertEqual(rows[0]['updated_at'],'')
    def test_review_predating_source_access_rejected(self):
        p=seed(self.root/'review-clock');v=native.read_json(p/'semantic-review.json');v['reviewed_at']='2026-10-05';write(p/'semantic-review.json',v);complete(p)
        self.assertIn('predates',str(native.validate(p)))
    def test_portable_name_device_and_alias_rejected(self):
        for name in ['notes/CON.md','notes/a.md:stream','notes/a.md.','notes/../report.md']:
            with self.assertRaises(ValueError):self.room.checked_name(name)
        files=dict(self.v['files']);files['Report.md']='Alias'
        with self.assertRaises(ValueError):self.room.save(self.v['key'],files,self.v['revision'])
    def test_malformed_request_body(self):
        with self.assertRaisesRegex(ValueError,'object'):self.room.request('POST','/api/create',[])
    def test_ordinary_write_failure_restores_prior_bytes(self):
        path=self.room.directory(self.v['key']);before={p.relative_to(path):p.read_bytes() for p in native_files(path)};files=dict(self.v['files']);files['research-brief.md']+='\nUseful update.';real=campaign.atomic;hit=[False]
        def failing(p,value):
            if Path(p).parent==path and Path(p).name=='coverage-matrix.md' and not hit[0]:hit[0]=True;raise OSError('injected ordinary write failure')
            return real(p,value)
        with patch.object(campaign,'atomic',side_effect=failing):
            with self.assertRaisesRegex(ValueError,'prior native files restored'):self.room.save(self.v['key'],files,self.v['revision'])
        self.assertEqual(before,{p.relative_to(path):p.read_bytes() for p in native_files(path)})

from evidence_contract import native_files
if __name__=='__main__':unittest.main()
