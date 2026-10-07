from pathlib import Path
import shutil,tempfile,sys,unittest
R=Path(__file__).parents[1];sys.path.insert(0,str(R/'scripts'))
from validate_release import validate
from product_files import inventory
class ReleaseValidatorProfileTests(unittest.TestCase):
    def test_source_ignores_retained_historical_state(self):
        errors,_,profile=validate(R,'source');self.assertEqual(profile,'source');self.assertEqual(errors,[])
    def test_complete_runtime_rejects_missing_advertised_room(self):
        with tempfile.TemporaryDirectory() as tmp:
            target=Path(tmp)/'product'
            for p in inventory(R):
                q=target/p.relative_to(R);q.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,q)
            self.assertEqual(validate(target,'runtime')[0],[])
            (target/'workspace/app.js').unlink()
            self.assertIn('missing workspace/app.js',validate(target,'runtime')[0])
if __name__=='__main__':unittest.main()
