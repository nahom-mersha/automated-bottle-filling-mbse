from pathlib import Path

from src import validate_traceability


VALID_CSV = """req_id,requirement_name,component,verification_method,status
R-001,detectBottleBeforeFilling,bottleSensor,model inspection,defined
R-002,positionBottleBeforeFilling,conveyor,model inspection,defined
R-003,fillBottleToTargetVolume,fillingUnit,conceptual analysis,defined
R-004,measureFillLevel,fillLevelSensor,model inspection,defined
R-005,acceptOrRejectBottle,rejectMechanism,logic analysis,defined
R-006,stopOnEmergencyRequest,controller,timing analysis,defined
"""


def test_valid_traceability(tmp_path: Path, monkeypatch) -> None:
    csv_file = tmp_path / "traceability.csv"
    csv_file.write_text(VALID_CSV, encoding="utf-8")

    monkeypatch.setattr(
        validate_traceability,
        "TRACEABILITY_FILE",
        csv_file,
    )

    assert validate_traceability.validate_traceability() == []


def test_duplicate_requirement_id_is_detected(
    tmp_path: Path,
    monkeypatch,
) -> None:
    csv_file = tmp_path / "traceability.csv"
    csv_file.write_text(
        VALID_CSV.replace(
            "R-002,positionBottleBeforeFilling",
            "R-001,positionBottleBeforeFilling",
        ),
        encoding="utf-8",
    )

    monkeypatch.setattr(
        validate_traceability,
        "TRACEABILITY_FILE",
        csv_file,
    )

    errors = validate_traceability.validate_traceability()

    assert any("duplicate requirement ID" in error for error in errors)