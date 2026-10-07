"""Regression of declared timestamp ordering; fictional fixtures, not model trials."""
import unittest,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]/"scripts"))
from evidence_contract import clock,precedes,loads
class Chronology(unittest.TestCase):
    def test_same_day_precise_order(self):
        self.assertTrue(precedes('2026-10-06T08:00:00Z','2026-10-06T23:00:00Z'))
    def test_offset_orders_instants(self):
        self.assertFalse(precedes('2026-10-06T20:00:00-10:00','2026-10-07T01:00:00Z'))
    def test_cutoff_applies_to_exact_timestamp(self):
        self.assertTrue(precedes('2026-10-06T12:00:00Z','2026-10-06T15:00:00Z'))
    def test_date_only_preserves_day_precision(self):
        self.assertFalse(precedes('2026-10-06','2026-10-06T23:00:00Z'))
        self.assertTrue(precedes('2026-10-05','2026-10-06'))
    def test_unknown_offset_not_utc(self):
        self.assertIsNone(clock('2026-10-06T23:00:00-00:00'))
        self.assertIsNotNone(clock('2026-10-06T23:00:00+00:00'))
class FiniteJSON(unittest.TestCase):
    def test_exponent_overflow_is_not_an_unlimited_budget(self):
        for value in ['1e400','-1e400','NaN','Infinity']:
            with self.assertRaisesRegex(ValueError,'non-finite JSON'):
                loads('{"budgets":{"tokens":'+value+'}}')
    def test_finite_fraction_and_null_survive(self):
        self.assertEqual(loads('{"hours":0.5,"tokens":null}'),{'hours':0.5,'tokens':None})
if __name__=='__main__':unittest.main()
