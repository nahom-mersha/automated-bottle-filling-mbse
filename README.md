# Automated Bottle Filling Station — SysML v2/MBSE Mini Project

## 1. Project Objective

This project develops a small Model-Based Systems Engineering (MBSE) model of a simplified automated bottle-filling station.

The station is intended to:

1. receive and detect a bottle;
2. position the bottle correctly;
3. fill it with a target quantity;
4. check the fill level;
5. accept or reject the bottle;
6. communicate its operating and fault status;
7. respond safely to an emergency-stop request.

The purpose of the project is to demonstrate how requirements, system structure, behaviour, and verification can be connected in one coherent model. A small Python validator will additionally check the consistency of the requirement-to-component-to-verification relationships.

This is a conceptual learning project. It does not represent an actual Krones machine and is not intended for industrial production, safety certification, or physical implementation.

## 2. Stakeholders

| Stakeholder | Main interest |
|---|---|
| Production operator | Easy operation, clear status information, and safe stopping |
| Maintenance technician | Understandable components, fault information, and diagnosability |
| Production manager | Reliable operation, acceptable throughput, and low rejection rates |
| Safety responsible stakeholder | Clear emergency-stop behaviour and safe operating assumptions |
| Systems engineer | Consistent requirements, system structure, behaviour, and verification traceability |
| Model reviewer | A clear, understandable, and internally consistent systems model |

## 3. System Boundary

### 3.1 System of interest

The system of interest is the automated bottle-filling station. It includes:

- conveyor;
- bottle-detection sensor;
- filling unit;
- fill-level sensor;
- accept/reject mechanism;
- controller;
- operator interface or status indicator;
- emergency-stop device.

### 3.2 External entities

The following entities interact with the station but are outside its system boundary:

- production operator;
- upstream bottle supply;
- downstream packaging or collection system;
- factory power and compressed-air supply;
- maintenance personnel;
- wider factory-control systems.

### 3.3 Included behaviour

The model covers:

- receiving and detecting a bottle;
- positioning the bottle;
- filling the bottle;
- checking the fill level;
- accepting or rejecting the bottle;
- reporting operating and fault states;
- responding to an emergency-stop request.

### 3.4 Excluded behaviour and implementation detail

The model does not cover:

- detailed mechanical dimensions;
- electrical circuit design;
- PLC implementation;
- fluid-dynamics simulation;
- conveyor motor sizing;
- industrial safety certification;
- physical hardware construction;
- integration with a real factory;
- detailed downstream packaging operations.

## 4. Initial Assumptions

- The station processes one bottle at a time in the simplified normal-flow scenario.
- The bottle has a conceptual nominal fill volume, such as 500 mL.
- Numerical values used later are learning assumptions, not official industrial specifications.
- Sensors and actuators are represented abstractly.
- Verification is performed through model inspection, analysis, or conceptual test cases rather than physical testing.