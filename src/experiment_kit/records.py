"""Common research record v1; independent of model family."""
from __future__ import annotations

import re
from typing import Any


def validate_record(record: Any) -> list[str]:
    if not isinstance(record, dict):
        return ["record must be an object"]
    issues: list[str] = []
    if type(record.get("schema_version")) is not int or record["schema_version"] != 1:
        issues.append("schema_version must be 1")
    for key in ("experiment_id", "kind", "objective", "code_ref"):
        if not isinstance(record.get(key), str) or not record[key].strip():
            issues.append(f"{key} must be a non-empty string")
    if type(record.get("seed")) is not int or record["seed"] < 0:
        issues.append("seed must be a non-negative integer")
    inputs = record.get("inputs")
    if not isinstance(inputs, list):
        issues.append("inputs must be a list")
    else:
        for index, item in enumerate(inputs):
            if not isinstance(item, dict):
                issues.append(f"inputs[{index}] must be an object")
                continue
            if not isinstance(item.get("uri"), str) or not item["uri"].strip():
                issues.append(f"inputs[{index}].uri must be a non-empty string")
            if not isinstance(item.get("sha256"), str) or not re.fullmatch(r"[0-9a-f]{64}", item["sha256"]):
                issues.append(f"inputs[{index}].sha256 must be a lowercase SHA-256")
    resources = record.get("resources")
    if not isinstance(resources, dict):
        issues.append("resources must be an object")
    else:
        if resources.get("device") not in ("cpu", "cuda", "mps"):
            issues.append("resources.device must be cpu, cuda, or mps")
        gpus = resources.get("gpus")
        if type(gpus) is not int or gpus < 0:
            issues.append("resources.gpus must be a non-negative integer")
        elif resources.get("device") == "cpu" and gpus != 0:
            issues.append("CPU records must declare zero GPUs")
        elif resources.get("device") in ("cuda", "mps") and gpus < 1:
            issues.append("accelerator records must declare at least one GPU")
    return issues
