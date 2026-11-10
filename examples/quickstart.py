from experiment_kit import validate_record
record = {"schema_version": 1, "experiment_id": "cpu-demo", "kind": "tabular", "objective": "Demonstrate CPU metadata", "code_ref": "your-repository@your-commit", "seed": 0, "inputs": [], "resources": {"device": "cpu", "gpus": 0}}
assert validate_record(record) == []
print("CPU record valid")
