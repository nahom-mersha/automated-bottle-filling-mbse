# Verification Matrix

This matrix records the conceptual verification approach used for the six requirements in the model.

It is a model-based review aid, not a physical test report or safety certification document.

| Requirement | Requirement name | Responsible component | Conceptual verification method |
|---|---|---|---|
| R-001 | detectBottleBeforeFilling | bottleSensor | Inspect the requirement-to-component satisfy relationship and review the operational action flow |
| R-002 | positionBottleBeforeFilling | conveyor | Inspect the structural model and verify the ordering in the action flow |
| R-003 | fillBottleToTargetVolume | fillingUnit | Review the requirement value, filling-unit allocation, and model traceability |
| R-004 | measureFillLevel | fillLevelSensor | Inspect the measurement action and its connection to the fill-level sensor |
| R-005 | acceptOrRejectBottle | rejectMechanism | Review the branching behaviour and the satisfy relationship to the sorting requirement |
| R-006 | stopOnEmergencyRequest | emergencyStop | Inspect the emergency-stop connection and the corresponding requirement traceability |

## Validation Scope

The Python validator checks the exported CSV traceability data for:

- required columns;
- non-empty values;
- unique requirement IDs; and
- the expected requirement set.

It does not currently parse the SysON ZIP export directly. The SysML model itself was reviewed through the SysON diagrams, requirements table, and model export.