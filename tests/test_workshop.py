import copy
import json
from pathlib import Path
import tempfile
import unittest
import workshop

class Checks(unittest.TestCase):
    def setUp(self):
        self.good=json.loads((workshop.ROOT/'examples/summary.good.json').read_text())
    def test_good_and_bad(self):
        self.assertEqual(workshop.validate(self.good), [])
        self.assertTrue(workshop.check(workshop.ROOT/'examples/summary.bad.json'))
    def test_missing_duplicate_and_invented(self):
        for mutation in ('missing','duplicate','invented','decision','type'):
            v=copy.deepcopy(self.good)
            if mutation=='missing': v['actions'].pop()
            if mutation=='duplicate': v['actions'][2]=v['actions'][0]
            if mutation=='invented': v['actions'][2]['due']='2026-09-12'
            if mutation=='decision': v['decision']='Approved'
            if mutation=='type': v['actions'][0]['evidence']=[]
            self.assertTrue(workshop.validate(v), mutation)
    def test_order_is_not_meaning(self):
        self.good['actions'].reverse()
        self.assertEqual(workshop.validate(self.good), [])
    def test_invalid_json_and_absent(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'bad.json'; p.write_text('{')
            self.assertTrue(workshop.check(p))
            self.assertTrue(workshop.check(Path(d)/'missing.json'))

class FollowupChecks(unittest.TestCase):
    def test_decision_failures(self):
        good=json.loads((workshop.ROOT/'examples/followups.good.json').read_text())
        self.assertEqual(workshop.validate_followups(good), [])
        for index, field, value in [(1,'owner','Luis'),(2,'owner','Alex'),(3,'status','READY'),(3,'owner','Priya'),(1,'evidence',['F2']),(0,'due','UNKNOWN')]:
            bad=copy.deepcopy(good);bad[index][field]=value
            self.assertTrue(workshop.validate_followups(bad), (index,field))
        self.assertTrue(workshop.validate_followups(good[:3]))
        self.assertTrue(workshop.validate_followups([good[0]]*4))
