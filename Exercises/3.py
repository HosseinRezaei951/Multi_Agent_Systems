# Import necessary libraries
from itertools import combinations
import math

# Reading game data file
'''
    game data file should have 2 line 
    first line: number of players
    second line: values for each coalition in game that separated by comma

    example:
    ---------------------------
    3
    0, 0, 0, 0.25, 0.5, 0.75, 1
    ---------------------------
    ==> this example meaning that:
        1) number of players = 3
        2) v(1)=v(2)=v(3)=0 , v(1,2)=0.25, v(1,3)=0.5, v(2,3)=0.75, v(1,2,3)=1
'''
file = open("data/game1.txt", "r") # data/game1.txt or data/game2.txt or data/game3.txt
file_data = file.read()
file_data = file_data.split()
game_data = [x.replace(",","") for x in file_data]

# Getting number of players
number_of_players = int(game_data.pop(0))

# Getting all combinations of [players] 
players = [x+1 for x in range(number_of_players)]
combinations_of_players = []
for i in range(number_of_players):
    comb = list(combinations(players, i+1))
    combinations_of_players.extend(comb)

# Making coalition-value dictionary
coalitions_dict = {():float(0)}
for i in range(len(combinations_of_players)):
    coalitions_dict[combinations_of_players[i]] = float(game_data[i])
print(f"\ncoalitions_dict:\n{coalitions_dict}\n")


# Function for getting all coalitions without special player
def get_coalitions_withOut_player(coalitions_dict, player):
    coalitions_withOut_player = []
    for key, value in coalitions_dict.items():
        if player not in key:
            coalitions_withOut_player.append({key:value})
    return coalitions_withOut_player

# Function for getting all coalitions union with special player
def get_coalitions_unionWith_player(game_value_dict, player):
    coalitions_withOut_player = []
    for key, value in coalitions_dict.items():
        if player in key:
            coalitions_withOut_player.append({key:value})
    return coalitions_withOut_player


# Calculating Shapley values for each player
for player in players:
    shaply_value = 1 / math.factorial(number_of_players)
    
    coalitions_withOut_player = get_coalitions_withOut_player(coalitions_dict, player)
    # print(f"coalitions_withOut_player({player}):\n{coalitions_withOut_player}")

    coalitions_unionWith_player = get_coalitions_unionWith_player(coalitions_dict, player)
    # print(f"coalitions_unionWith_player({player}):\n{coalitions_unionWith_player}")

    summation = 0
    for i in range(len(coalitions_withOut_player)):
        S_size = len(list(coalitions_withOut_player[i].keys())[0])
        V_SUi = list(coalitions_unionWith_player[i].values())[0]
        V_S = list(coalitions_withOut_player[i].values())[0]
        summation += (math.factorial(S_size)*\
                math.factorial((number_of_players-1)-S_size)*\
                (V_SUi - V_S))
    
    shaply_value = shaply_value * summation
    print(f"Shapley value for player({player}): {shaply_value}")
