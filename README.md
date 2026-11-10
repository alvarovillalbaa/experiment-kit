# experiment-kit

Last updated: 2026-11-10

Validate reproducible research records independently of training frameworks.

**Status: implemented.** A standard-library Python 3.11+ library and CLI are present. Installation/build proof is recorded separately from source checks.

## Independent use

From this repository:

```sh
python3 -m pip install .
python3 -m experiment_kit.cli examples/cpu.json --profile record
python3 examples/quickstart.py
```

No sibling checkout, GPU, account, database, or network service is needed for these examples.

## Ownership

Common experiment metadata and the separate legacy LLM spec profile.

Outside this component: Dataset processing, model execution, scheduling, or scoring.

## Compose

Use independently, or register a pinned version in [Lab](https://github.com/alvarovillalbaa/lab). A dependency on Lab is never required. Libraries connect through declared dependencies or explicit artifact/job interfaces.

[Specification and next work](docs/specs/README.md) · [Extraction provenance](docs/sources/lab-provenance.json)

MIT applies to the code and authored documentation in this repository. External datasets, model weights, provider services, and third-party projects retain their own terms.

`validate_record` checks common record v1; `validate_spec` retains the legacy LLM profile. Common records require schema_version, experiment_id, kind, objective, code_ref, seed, inputs (URI/SHA-256 pairs), and resources (device/GPU count). They do not execute code or verify remote input bytes. LLM example configs are frozen test fixtures; integrated experiment configurations are maintained in Lab.
