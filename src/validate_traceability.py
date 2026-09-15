import csv
from pathlib import Path


TRACEABILITY_FILE = (
    Path(__file__).resolve().parents[1] / "data" / "traceability.csv"
)

REQUIRED_COLUMNS = {
    "req_id",
    "requirement_name",
    "component",
    "verification_method",
    "status",
}

EXPECTED_REQUIREMENT_IDS = {
    "R-001",
    "R-002",
    "R-003",
    "R-004",
    "R-005",
    "R-006",
}


def validate_traceability() -> list[str]:
    errors: list[str] = []

    if not TRACEABILITY_FILE.exists():
        return [f"File not found: {TRACEABILITY_FILE}"]

    with TRACEABILITY_FILE.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames is None:
            return ["CSV file has no header row."]

        missing_columns = REQUIRED_COLUMNS - set(reader.fieldnames)
        if missing_columns:
            errors.append(
                f"Missing columns: {', '.join(sorted(missing_columns))}"
            )

        seen_ids: set[str] = set()

        for line_number, row in enumerate(reader, start=2):
            for column in REQUIRED_COLUMNS:
                if not row.get(column, "").strip():
                    errors.append(
                        f"Line {line_number}: '{column}' must not be empty."
                    )

            req_id = row.get("req_id", "").strip()

            if req_id in seen_ids:
                errors.append(f"Line {line_number}: duplicate requirement ID '{req_id}'.")
            seen_ids.add(req_id)

        missing_ids = EXPECTED_REQUIREMENT_IDS - seen_ids
        unexpected_ids = seen_ids - EXPECTED_REQUIREMENT_IDS

        if missing_ids:
            errors.append(
                f"Missing requirement IDs: {', '.join(sorted(missing_ids))}"
            )

        if unexpected_ids:
            errors.append(
                f"Unexpected requirement IDs: {', '.join(sorted(unexpected_ids))}"
            )

    return errors


def main() -> int:
    errors = validate_traceability()

    if errors:
        print("Traceability validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Traceability validation passed: six requirements checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())