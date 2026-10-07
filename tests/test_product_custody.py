import json,os,shutil,subprocess,sys,tempfile,unittest,zipfile
from pathlib import Path
R=Path(__file__).parents[1];sys.path.insert(0,str(R/'scripts'))
from custody import namespace,reject_links,tree_files
from product_files import inventory
from build_workspace_release import build
from validate_release import validate
class ProductCustodyTests(unittest.TestCase):
    def test_portable_aliases_and_file_directory_conflict(self):
        for names in [[('report.md',False),('REPORT.md',False)],[('a',False),('a/b',False)],[('con.md',False)],[('notes/e\u0301.md',False),('notes/é.md',False)],[('notes/'+('z'*256)+'.md',False)]]:
            with self.assertRaises(ValueError):namespace(names)
    def test_help_is_readonly(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=subprocess.run([sys.executable,'-B',str(R/'scripts/build_workspace_release.py'),'--help'],cwd=tmp,capture_output=True,text=True);self.assertEqual(p.returncode,0);self.assertEqual(list(Path(tmp).iterdir()),[])
    def test_existing_candidate_preserved(self):
        with tempfile.TemporaryDirectory() as tmp:
            out=Path(tmp)/'old';out.mkdir();(out/'prior.zip').write_bytes(b'accepted bytes')
            with self.assertRaisesRegex(ValueError,'output exists'):build(R,out)
            self.assertEqual((out/'prior.zip').read_bytes(),b'accepted bytes')
    def test_bad_source_rejected_without_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            base=Path(tmp);source=base/'source'
            for p in inventory(R):
                q=source/p.relative_to(R);q.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,q)
            (source/'workspace/app.js').unlink();out=base/'candidate'
            with self.assertRaisesRegex(ValueError,'app.js'):build(source,out)
            self.assertFalse(out.exists())
    def test_junction_root_refused_before_resolution(self):
        if os.name!='nt':self.skipTest('Windows junction case')
        with tempfile.TemporaryDirectory() as tmp:
            base=Path(tmp);real=base/'actual';real.mkdir();(real/'private.txt').write_text('outside owned tree');link=base/'linked'
            env=dict(os.environ,OMNARA_TEST_LINK=str(link),OMNARA_TEST_TARGET=str(real))
            p=subprocess.run(['powershell','-NoProfile','-Command','New-Item -ItemType Junction -Path $env:OMNARA_TEST_LINK -Target $env:OMNARA_TEST_TARGET | Out-Null'],env=env,capture_output=True,text=True)
            if p.returncode:self.skipTest('junction unavailable: '+p.stderr)
            with self.assertRaisesRegex(ValueError,'reparse'):reject_links(link)
            with self.assertRaisesRegex(ValueError,'reparse'):tree_files(base)
            # rmdir removes only this exact test junction, not the external target.
            link.rmdir();self.assertEqual((real/'private.txt').read_text(),'outside owned tree')
if __name__=='__main__':unittest.main()
