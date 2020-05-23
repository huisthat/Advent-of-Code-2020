# find where the wire passes
# put it in a list for each wire
# find the intersection points
# find the closest

with open("day3.txt", "r") as file:
    line = file.readlines()

line[0] = line[0].strip('\n')

def split_values(line):
    directions = line.split(',')
    return directions

#moves is the directions of one wire
def move(moves):
    coordinates = [0, 0]
    passed_by = []
    for i in moves:
        if i[0] == 'R':
            for step in range(int(i[1:])):
                step = (coordinates[0]+1, coordinates[1])
                passed_by.append(step)
                coordinates[0] += 1
                
        elif i[0] == 'L':
            for step in range(int(i[1:])):
                step = (coordinates[0]-1, coordinates[1])
                passed_by.append(step)
                coordinates[0] -= 1
                
        elif i[0] == 'U':
            for step in range(int(i[1:])):
                step = (coordinates[0], coordinates[1]+1)
                passed_by.append(step)
                coordinates[1] += 1
                
        elif i[0] == 'D':
            for step in range(int(i[1:])):
                step = (coordinates[0], coordinates[1]-1)
                passed_by.append(step)
                coordinates[1] -= 1
    return passed_by


wire1_locations = move(split_values(line[0]))
wire2_locations = move(split_values(line[1]))

intersections = set(wire1_locations).intersection(set(wire2_locations))

steps = []
for coordinates in intersections:
    step = wire1_locations.index(coordinates) + wire2_locations.index(coordinates) + 2
    steps.append(step)

steps.sort()
print(steps[0])
