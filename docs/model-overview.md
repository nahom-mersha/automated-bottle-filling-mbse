# Model Overview

## Purpose

This project is a conceptual Model-Based Systems Engineering (MBSE) model of an automated bottle-filling station. It demonstrates how requirements, system structure, behaviour, and verification-related information can be connected in a small SysML v2 model.

The model was created in Eclipse SysON.

## System Structure

The system of interest is `AutomatedBottleFillingStation`.

It contains eight conceptual parts:

- `conveyor`
- `bottleSensor`
- `fillingUnit`
- `fillLevelSensor`
- `rejectMechanism`
- `controller`
- `operatorInterface`
- `emergencyStop`

The component-interconnection view contains seven named connections:

- `conveyorBottleLink`
- `bottleDetectionLink`
- `fillLevelFeedbackLink`
- `emergencyStopLink`
- `operatorStatusLink`
- `controllerFillingLink`
- `rejectControlLink`

## Requirements

The model contains six requirements:

- `R-001` — Detect a bottle before filling
- `R-002` — Position a bottle before filling
- `R-003` — Fill a bottle to the target volume
- `R-004` — Measure the fill level
- `R-005` — Accept or reject the bottle based on the fill level
- `R-006` — Stop the station after an emergency-stop request

The target volume and timing values are conceptual learning assumptions, not industrial specifications.

## Behaviour

The operational behaviour is represented by the `bottleProcessingFlow` action flow:

1. `receiveBottle`
2. `detectBottle`
3. `positionBottle`
4. `fillBottle`
5. `measureFillLevel`
6. `acceptBottle` or `rejectBottle`
7. `reportStatus`

The flow contains eight actions and eight succession relationships.

## Traceability

Satisfy relationships connect relevant system parts to requirements. The exported requirements and traceability data are stored in the `data/` directory.

The model is intended to demonstrate traceability across:

- requirements;
- system structure;
- component responsibilities;
- operational behaviour; and
- conceptual verification methods.