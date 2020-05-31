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

def count_asteroid(coordinates, list_coordinates):
    angles = {}
    for i in list_coordinates:
        if coordinates != i:
            x_increase = i[0] - coordinates[0]
            y_increase = -i[1] + coordinates[1]
            angle = round(math.atan2(y_increase, x_increase), 10) - round((math.pi / 2), 10)
            if angle < 0:
                angle += (2 * math.pi)
            new_angle = round(angle, 4)
            if new_angle not in angles.keys():
                angles[new_angle] = i
            else:
                i_distance = abs(x_increase) + abs(y_increase)
                key_distance = abs(angles[new_angle][0] - coordinates[0]) + abs(angles[new_angle][1] - coordinates[1])
                if i_distance < key_distance:
                    angles[new_angle] = i
        
    return len(angles), angles


for asteroid in asteroid_coordinates:
    number, angle_dictionary = count_asteroid(asteroid, asteroid_coordinates)

    if number == 334: # 334 is the max_number of asteroids
        angle_list = []
        for k in angle_dictionary.keys():
            angle_list.append(k)
        angle_list.sort(reverse=True)
        angle = angle_list[198]
        print(angle_dictionary)
        for k, v in angle_dictionary.items():
            if k == angle:
                print(v)
