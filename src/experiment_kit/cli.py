"""Explicit validation profiles; this command does not execute experiments."""
import argparse
import json
import sys

from . import validate_record, validate_spec


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("spec")
    parser.add_argument("--profile", choices=("llm", "record"), default="llm")
    args = parser.parse_args(argv)
    try:
        with open(args.spec, encoding="utf-8") as handle:
            spec = json.load(handle)
        if not isinstance(spec, dict):
            raise ValueError("spec must be a JSON object")
        issues = (validate_spec if args.profile == "llm" else validate_record)(spec)
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    for issue in issues:
        print(f"ERROR: {issue}", file=sys.stderr)
    if issues:
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
