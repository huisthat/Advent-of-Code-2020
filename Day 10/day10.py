import math

with open("day10.txt") as f:
	grid = f.readlines()

for i in range(len(grid)):
    grid[i] = grid[i].strip('\n')

max_length = len(grid[0])
max_height = len(grid)

asteroid_coordinates = []

for line in grid:
    for character_index in range(len(line)):
        if line[character_index] == '#':
            coordinates = (character_index, grid.index(line))
            asteroid_coordinates.append(coordinates)

print(asteroid_coordinates)

def count_asteroid(coordinates, list_coordinates):
    angles = set()
    for i in list_coordinates:
        if coordinates != i:
            x_increase = i[0] - coordinates[0]
            y_increase = i[1] - coordinates[1]
            angle = math.atan2(y_increase, x_increase)
            angles.add(round(angle, 4))
    
    return len(angles)


max_number = 0
for asteroid in asteroid_coordinates:
    number = count_asteroid(asteroid, asteroid_coordinates)
    if number > max_number:
        max_number = number

print(max_number)

