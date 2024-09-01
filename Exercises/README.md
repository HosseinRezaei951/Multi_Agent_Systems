# Game Theory Course - Exercises

## Overview

This repository contains the code and resources for the exercises related to Cooperative Game Theory. The exercises utilize Python libraries such as `axelrod` and `itertools` to implement and analyze various game theory strategies and concepts. Below is an explanation of the exercises and how to run the provided scripts.

## Exercises

### Exercise 2: Tournament Analysis of Strategies

**Objective**: Use the `axelrod` Python library to simulate and compare the performance of different strategies in a tournament setting. The goal is to experimentally determine if the strategy `AllD` (always defect) performs better or at least equally well compared to other strategies.

**Strategies**:
- **AllC**: Always cooperate.
- **AllD**: Always defect.
- **Grim**: Cooperate until the other agent defects, then defect forever.
- **Tit-for-Tat (TFT)**: On the first move, cooperate. On subsequent moves, repeat the opponent’s previous move.
- **Tit-for-Two-Tats (TFTT)**: Similar to TFT but only retaliates if the opponent defects twice in a row.
- **Tester**: Defect on the first round. If the opponent retaliates, play TFT. Otherwise, alternate between cooperating and defecting.
- **Pavlov**: Cooperate on the first round. After that, if you win, use the same action on the next round; if you lose, switch to the other action.

**Instructions**:
1. Navigate to the `2.py` and `2_2.py` files to see the tournament setup.
2. `2.py` runs a tournament with a specific set of strategies including AllC, AllD, Grim, TFT, TFTT, Tester, and Pavlov.
3. `2_2.py` runs a second tournament with a different set of strategies, focusing on the performance of `AllD` against other adaptive strategies.
4. The results of each tournament are saved as CSV files in the `results` directory, and the performance is visualized in a plot.

**Files**:
- `2.py`: Runs the first tournament.
- `2_2.py`: Runs the second tournament.
- `results/2(tornoment_results).csv`: Results of the first tournament.
- `results/2_2(tornoment_results).csv`: Results of the second tournament.
- `results/2(winplot).png`: Plot showing the win distribution for the first tournament.
- `results/2_2(winplot).png`: Plot showing the win distribution for the second tournament.

### Exercise 3: Shapley Value Calculation

**Objective**: Write a Python script to compute the Shapley value for each player in a cooperative game based on given coalition values.

**Instructions**:
1. The script reads input from a text file (`game1.txt`, `game2.txt`, or `game3.txt`) located in the `data` directory.
2. The input file should contain two lines:
   - The first line specifies the number of players.
   - The second line lists the values for each coalition in the game, separated by commas.
3. The script calculates the Shapley value for each player based on the provided coalition values and outputs the results.

**Example Input Format**:
```
3
0, 0, 0, 0.25, 0.5, 0.75, 1
```
- `3` players.
- Coalition values: V(1) = 0, V(2) = 0, V(3) = 0, V(1,2) = 0.25, V(1,3) = 0.5, V(2,3) = 0.75, V(1,2,3) = 1.

**Files**:
- `3.py`: The script for calculating Shapley values.
- `data/game1.txt`, `data/game2.txt`, `data/game3.txt`: Example game data files.

## How to Run

1. **Setup**: Ensure you have Python installed. Install the `axelrod` library for running the tournaments:
   ```
   pip install axelrod
   ```
2. **Run Tournament**:
   - Navigate to the directory containing `2.py` or `2_2.py`.
   - Run the script:
     ```
     python 2.py
     ```
   - Results will be saved in the `results` folder.

3. **Calculate Shapley Value**:
   - Navigate to the directory containing `3.py`.
   - Run the script with one of the provided game data files:
     ```
     python 3.py
     ```
   - The script will print the Shapley values for each player.

## Notes

- Ensure the `data` and `results` directories are present in the same directory as the scripts.
- Modify the input data files in the `data` directory to experiment with different coalition values and player numbers.
