# Wireless Sensor Tracking System (WST) Using CSP for Multi-Agent Systems

This project is part of the **Multi-Agent Systems Course** and focuses on the implementation of a Wireless Sensor Tracking System (WST) using Constraint Satisfaction Problem (CSP) techniques. The objective is to model and solve the problem of tracking multiple moving targets using a network of wireless sensors. The sensors must collaborate to track the targets while adhering to specific communication and visibility constraints.

## Problem Definition

The WST system consists of a network of \(n\) sensors \(S = \{S_1, S_2, \dots, S_n\}\) that track a set of \(m\) moving targets \(T = \{t_1, t_2, \dots, t_m\}\). Each sensor has a circular coverage area with a radius \(R\), within which it can detect targets. To accurately determine the position of a target, the position and speed data from \(k\) sensors need to be combined. However, each sensor can participate in tracking only one target at a time, despite possibly being within the range of multiple targets.

Due to bandwidth and power limitations, sensors cannot communicate with all other sensors in the network; they can only communicate with a limited number of nearby sensors. Sensors that have direct communication links can cooperate to track a specific target.

The problem is modeled as a CSP, where the input is a graph representing sensor-target visibility and sensor-sensor communication. The visibility graph is represented by a matrix where each element indicates whether a target is visible to a sensor. Similarly, a communication matrix is used to represent the communication capability between sensors.

## Solution Approach

### Constraint Satisfaction Problem (CSP) Formulation

The CSP formulation for the WST system involves assigning \(k\) sensors to each target such that:
1. **Visibility Constraint**: A sensor can only be assigned to a target if it is within the sensor's visibility range.
2. **Communication Constraint**: Sensors assigned to the same target must be able to communicate with each other.
3. **Assignment Constraint**: Each sensor can only track one target at a time.

### Implementation Overview

The solution is implemented in Python with the following modules:

- **CSP Module (`csp.py`)**: Handles the CSP logic, including sensor creation, matrix generation, and the CSP solving process.
- **Sensor Module (`sensor.py`)**: Defines the sensor class, including methods for determining visibility, connectivity, and target locking.
- **Target Module (`target.py`)**: Defines the target class, which includes properties such as position and unique identifiers.
- **Tools Module (`tools.py`)**: Provides utility functions, such as calculating the Euclidean distance between points.

### Execution Flow

1. **Initialization**: The sensor positions, coverage radius, and target positions are initialized.
2. **Communication and Visibility Matrix Generation**: The communication matrix is generated based on the sensor positions, and the visibility matrix is updated as new targets are introduced.
3. **CSP Execution**: The CSP is solved iteratively for each target, updating the visibility matrix to reflect sensor-target assignments.
4. **Output**: The final visibility matrix, indicating which sensors are tracking which targets, is printed.

## Directory Structure

- **assets**
  - `csp.py`: Contains the CSP class and related methods for sensor-target assignment.
  - `sensor.py`: Defines the Sensor class and handles visibility and communication checks.
  - `target.py`: Defines the Target class with properties for position and identification.
  - `tools.py`: Includes utility functions such as Euclidean distance calculation.
- **results**
  - `1.txt`: Stores the output from the CSP process.
- `main.py`: The main entry point for the program, which sets up the problem, runs the CSP process, and outputs the results.

## How to Use

1. **Run the Program**: Execute the `main.py` script to initialize the sensors, targets, and run the CSP algorithm.
2. **Inspect the Results**: The program outputs the communication matrix and visibility matrix before and after running the CSP process. The final visibility matrix shows which sensors are assigned to track each target.

## Example Execution

In the provided example, the grid of sensors is arranged as follows:

```
Sensors position:
    S1  S2  S3
    S4  S5  S6
    S7  S8  S9
    S10 S11 S12
```

Two targets are positioned at `(1.5, 1)` and `(2.5, 1)`. The program tracks these targets by assigning the required number of sensors based on the visibility and communication constraints.

## Conclusion

This project demonstrates how CSP can be applied to solve a real-world problem in a multi-agent system, specifically for tracking moving targets using a network of wireless sensors. The solution efficiently assigns sensors to targets while respecting both visibility and communication constraints, ensuring reliable tracking.