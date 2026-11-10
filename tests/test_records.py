import copy
import json
import unittest
from pathlib import Path
from experiment_kit import validate_record


class RecordTests(unittest.TestCase):
    def setUp(self):
        self.record = json.loads((Path(__file__).resolve().parents[1] / "examples/cpu.json").read_text())

    def test_cpu_has_no_llm_requirements(self):
        self.assertEqual(validate_record(self.record), [])

    def test_malformed_records_fail(self):
        for field, value in [("seed", True), ("schema_version", True), ("inputs", [{"uri": "x", "sha256": "bad"}]), ("resources", {"device": "cpu", "gpus": 1})]:
            record = copy.deepcopy(self.record)
            record[field] = value
            with self.subTest(field=field):
                self.assertTrue(validate_record(record))
        self.assertTrue(validate_record([]))


if __name__ == "__main__":
    unittest.main()
