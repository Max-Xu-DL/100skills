"""AIMax synthetic authorization reproduction and threat-record completeness checks.

Standard library only. No sockets, live credentials, customer files or exploit traffic.
The intentionally weak function exists solely for this in-memory before/after test.
"""
import copy
import json
from pathlib import Path
import platform

HERE = Path(__file__).resolve().parent
FILES = {"file-a": {"tenant": "agency-a", "content": "synthetic agency A brief"}}


def weak_download(authenticated_tenant, object_id):
    if not authenticated_tenant:
        return None
    return FILES.get(object_id)


def scoped_download(authenticated_tenant, object_id):
    record = FILES.get(object_id)
    if record is None or not authenticated_tenant or record["tenant"] != authenticated_tenant:
        return None
    return record


def validate_model(system, report):
    elements = {x["id"] for x in system["nodes"] + system["flows"]}
    expected = {(e, letter) for e in elements for letter in "STRIDE"}
    actual = {(x["element"], x["category"]) for x in report["coverage"]}
    coverage_ok = actual == expected and len(report["coverage"]) == len(expected)
    actions_ok = all(all(t.get(k) for k in ("mitigation", "owner", "target_date", "validation")) for t in report["threats"])
    return coverage_ok and actions_ok


def main():
    system = json.loads((HERE / "system.json").read_text())
    report = json.loads((HERE / "threat-model.json").read_text())
    checks = {
        "weak_cross_tenant_read_reproduced": weak_download("agency-b", "file-a") is not None,
        "scoped_cross_tenant_read_denied": scoped_download("agency-b", "file-a") is None,
        "scoped_same_tenant_read_allowed": scoped_download("agency-a", "file-a") == FILES["file-a"],
        "scoped_missing_file_denied": scoped_download("agency-a", "missing") is None,
        "scoped_unauthenticated_read_denied": scoped_download(None, "file-a") is None,
        "complete_coverage_and_action_records": validate_model(system, report),
    }
    negatives = []
    for label, change in [
        ("missing-owner", lambda x: x["threats"][0].pop("owner")),
        ("missing-target-date", lambda x: x["threats"][0].pop("target_date")),
        ("skipped-stride-cell", lambda x: x["coverage"].pop()),
    ]:
        mutant = copy.deepcopy(report)
        change(mutant)
        negatives.append({"case": label, "rejected": not validate_model(system, mutant)})
    result = {
        "method": "actual in-memory Python before/after reproduction plus authored report completeness checks",
        "python": platform.python_version(),
        "checks": checks,
        "negative_cases": negatives,
        "coverage_cells": len(report["coverage"]),
        "ranked_threat_records": len(report["threats"]),
        "passed": all(checks.values()) and all(x["rejected"] for x in negatives),
        "not_measured": ["production security", "independent model adherence", "host skill triggering", "all threats discovered", "cloud IAM enforcement", "Microsoft Threat Modeling Tool execution"],
    }
    (HERE / "results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
