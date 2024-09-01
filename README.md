# Multi-Agent Systems Course

Welcome to the Multi-Agent Systems Course repository. This repository contains a collection of exercises and a project designed to give hands-on experience with various concepts in multi-agent systems, including tournament strategies and Shapley value calculations, as well as collaborative filtering, constraint satisfaction, and sensor-target problems.

## Directory Structure

### Exercises

The `Exercises` directory includes multiple sub-directories, each focusing on different aspects of multi-agent systems, from strategic interactions to cooperative game theory.

#### Exercise 2: Tournament Analysis of Strategies

- **Sub-directory: results**
  - **2(tornoment_results).csv**: Results of the first tournament between various strategies.
  - **2(winplot).png**: Plot visualizing the win distribution for the first tournament.
  - **2_2(tornoment_results).csv**: Results of the second tournament focusing on `AllD` against adaptive strategies.
  - **2_2(winplot).png**: Plot visualizing the win distribution for the second tournament.

- **2.py**: Script to run the first tournament, comparing strategies like AllC, AllD, Grim, TFT, TFTT, Tester, and Pavlov.
- **2_2.py**: Script to run the second tournament, focusing on the performance of AllD against adaptive strategies.
- **README.md**: Overview and instructions for running the tournament analysis.

#### Exercise 3: Shapley Value Calculation

- **Sub-directory: data**
  - **game1.txt**: Game data file with coalition values for the first game.
  - **game2.txt**: Game data file with coalition values for the second game.
  - **game3.txt**: Game data file with coalition values for the third game.

- **3.py**: Script to calculate the Shapley value for each player based on the input game data.
- **README.md**: Overview and instructions for calculating the Shapley value.

### Project

The `Project` directory contains a collaborative filtering and constraint satisfaction problem project, including scripts and assets necessary to run simulations and analyze the results.

#### Project Files

- **Sub-directory: assets**
  - **csp.py**: Implementation of the Constraint Satisfaction Problem (CSP) model.
  - **sensor.py**: Script simulating sensor dynamics in the project.
  - **target.py**: Script managing target behaviors and interactions.
  - **tools.py**: Utility functions and tools used across the project.

- **Sub-directory: results**
  - **1.txt**: Results and output of the project simulations.

- **main.py**: The main script to run the project, bringing together the CSP model, sensors, and targets.
- **README.md**: Overview and instructions for running the project.

## How to Use

### Exercises

1. **Tournament Analysis (Exercise 2)**:
   - Navigate to the `Exercises` directory and explore `2.py` and `2_2.py` to understand the tournament setup and strategy comparisons.
   - Execute the scripts to run the tournaments and analyze the results.
   - Review the CSV files and plots in the `results` sub-directory to interpret the outcomes of the tournaments.

2. **Shapley Value Calculation (Exercise 3)**:
   - Navigate to the `Exercises/data` directory and review the provided game data files (`game1.txt`, `game2.txt`, `game3.txt`).
   - Execute `3.py` to calculate the Shapley values for each player based on the coalition values provided in the game data files.
   - The script will print the Shapley values for each player to the console.

### Project

1. **Project Overview**:
   - Navigate to the `Project` directory and review the `README.md` for an overview of the project.
   - Explore the `assets` sub-directory to understand the individual components such as CSP models, sensor dynamics, and target interactions.
   - Execute `main.py` to run the project simulation, which integrates all components.

2. **Results Analysis**:
   - Review the output in the `results/1.txt` file to analyze the outcomes of the simulation.

This course provides practical experience with key concepts in multi-agent systems, offering insights into both the strategic and cooperative aspects of multi-agent interactions and problem-solving.
