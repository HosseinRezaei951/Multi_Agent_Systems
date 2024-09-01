import math

def euclidean_distance(position1, position2):
    return math.sqrt((position1[0]-position2[0])**2 +
                     (position1[1]-position2[1])**2)