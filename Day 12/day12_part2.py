
import itertools
from itertools import combinations
from math import gcd


variations = list(combinations(range(4), 2))

position = [
            [4, 12, 13], 
            [-9, 14, -3],
            [-7, -1, 2],
            [-11, 17, -1]
            ]
initial_position = [
                    [4, 12, 13], 
                    [-9, 14, -3],
                    [-7, -1, 2],
                    [-11, 17, -1]
                    ]


velocity = [
            [0, 0, 0], 
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
            ]

initial_velocity = [
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


step = 1

axis_count = [0, 0, 0]

while True:
    apply_gravity()
    apply_velocity()

    for axis in range(3):
        count = 0
        for i in range(4):
            if position[i][axis] == initial_position[i][axis]:
                count += 1
            
            if velocity[i][axis] == initial_velocity[i][axis]:
                count += 1
        
        if count == 8:
            axis_count[axis] = step
    
    step += 1

    counts = 0
    for axis in axis_count:
        if axis != 0:
            counts += 1
    if counts == 3:
        break
    

print(axis_count)

def lcm(a):
    lcm = a[0]
    for i in a[1:]:
        lcm = lcm*i//gcd(lcm, i)
    return lcm

print(lcm(axis_count))