
import itertools
from itertools import combinations
# <x=4, y=12, z=13>
# <x=-9, y=14, z=-3>
# <x=-7, y=-1, z=2>
# <x=-11, y=17, z=-1>

variations = list(combinations(range(4), 2))

position = [
            [4, 12, 13], 
            [-9, 14, -3],
            [-7, -1, 2],
            [-11, 17, -1]
            ]

# position = [
#             [-1, 0, 2], 
#             [2, -10, -7],
#             [4, -8, 8],
#             [3, 5, -1]
#             ]

velocity = [
            [0, 0, 0], 
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
            ]

# need to do for all three axis 
def compare(p1, p2, v1, v2): 
    if p1 > p2:
        v1 -= 1
        v2 += 1
    
    elif p2 > p1:
        v1 += 1
        v2 -= 1
    
    return v1, v2

def get_position(moon_1, moon_2):
    position


def apply_gravity():
    for moon_combination in variations:
        moon_1 = moon_combination[0]
        moon_2 = moon_combination[1]
        for i in range(3):
            p1 = position[moon_1][i]
            p2 = position[moon_2][i]
            v1 = velocity[moon_1][i]
            v2 = velocity[moon_2][i]
            velocity[moon_1][i], velocity[moon_2][i] = compare(p1, p2, v1, v2)

def apply_velocity():
    for moon in range(4):
        for i in range(3):
            position[moon][i] += velocity[moon][i]

for i in range(1000):
    apply_gravity()
    apply_velocity()


total = 0

for moon in range(4):
    pot = 0
    kin = 0
    for axis in range(3):
        pot += abs(position[moon][axis])
        kin += abs(velocity[moon][axis])
    total += pot * kin

print(total)


    