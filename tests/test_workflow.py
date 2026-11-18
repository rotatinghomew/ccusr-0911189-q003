import copy
import json
from pathlib import Path
import subprocess
import sys
import unittest

from kiosk.workflow import report


class WorkflowTest(unittest.TestCase):
    def setUp(self):
        self.path = Path(__file__).resolve().parents[1] / 'data' / 'sample.json'
        self.data = json.loads(self.path.read_text(encoding='utf-8'))

    def test_entry(self):
        result = subprocess.run([sys.executable, '-m', 'kiosk', 'week', str(self.path)],
                                check=True, capture_output=True, text=True)
        self.assertEqual(json.loads(result.stdout), report(self.data))

    def test_calendar_and_substitution_receipt(self):
        summary = report(self.data)
        self.assertEqual(summary['open_item_days'], 4)
        self.assertEqual(summary['loan_totals'], {'A/atlas':1})
        self.assertEqual(summary['transport']['committed'], ['T1'])

    def test_conflicting_receipt(self):
        self.data['requests'][1]['loaned'] = 'story'
        with self.assertRaises(ValueError):
            report(self.data)
