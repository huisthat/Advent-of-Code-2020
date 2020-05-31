from collections import defaultdict

with open("day11.txt") as f:
	line = f.read()
	initial_list = line.split(',')



x = defaultdict(int)

for count, item in enumerate(initial_list):
    x[count] = item


i = 0
relative_base = 0

def run_programme(input_colour, i):
    global relative_base
    output_count = 0
    while output_count < 2:
        x[i] = str(x[i])
        while len(x[i]) < 5:
            x[i] = '0' + x[i]

        if x[i][3:] == '01':
            if x[i][2] == '0':
                first_number = int(x[int(x[i+1])])
            
            elif x[i][2] == '1': 
                first_number = int(x[i+1])
            
            elif x[i][2] == '2':
                first_number = int(x[int(x[i+1]) + relative_base])

            if x[i][1] == '0':
                second_number = int(x[int(x[i+2])])
            
            elif x[i][1] == '1': 
                second_number = int(x[i+2])
            
            elif x[i][1] == '2':
                second_number = int(x[int(x[i+2]) + relative_base])
            
            if x[i][0] == '0':
                index_to_replace = int(x[i+3])
            
            elif x[i][0] == '2':
                index_to_replace = int(x[i+3]) + relative_base

            x[index_to_replace] = first_number + second_number
            i += 4

        elif x[i][3:] == '02': 
            if x[i][2] == '0':
                first_number = int(x[int(x[i+1])])
            
            elif x[i][2] == '1': 
                first_number = int(x[i+1])
            
            elif x[i][2] == '2':
                first_number = int(x[int(x[i+1]) + relative_base])
            
            if x[i][1] == '0':
                second_number = int(x[int(x[i+2])])
            
            elif x[i][1] == '1': 
                second_number = int(x[i+2])

            elif x[i][1] == '2':
                second_number = int(x[int(x[i+2]) + relative_base])
            
            if x[i][0] == '0':
                index_to_replace = int(x[i+3])
            
            elif x[i][0] == '2':
                index_to_replace = int(x[i+3]) + relative_base

            x[index_to_replace] = first_number * second_number
            i += 4

        elif x[i][3:] == '03':
            if x[i][2] == '0':
                x[int(x[i+1])] = str(input_colour)
            
            elif x[i][2] == '2':
                x[int(x[i+1]) + relative_base] = str(input_colour)
            i += 2

        elif x[i][3:] == '04':
            if x[i][2] == '0':
                output = int(x[int(x[i+1])])

            elif x[i][2] == '1':
                output = int(x[i+1])
            
            elif x[i][2] == '2':
                output = int(x[int(x[i+1]) + relative_base])

            output_count += 1
            i += 2
        
        elif x[i][3:] == '05':
            if x[i][2] == '0':
                check = int(x[int(x[i+1])])
            
            elif x[i][2] == '1':
                check = int(x[i+1])
            
            elif x[i][2] == '2':
                check = int(x[int(x[i+1]) + relative_base])
            
            if check != 0:
                if x[i][1] == '0':
                    i = int(x[int(x[i+2])])

                elif x[i][1] == '1': 
                    i = int(x[i+2])
                
                elif x[i][1] == '2':
                    i = int(x[int(x[i+2]) + relative_base])

            else: 
                i += 3

        elif x[i][3:] == '06':
            if x[i][2] == '0':
                check = int(x[int(x[i+1])])
            
            elif x[i][2] == '1': 
                check = int(x[i+1])
            
            elif x[i][2] == '2':
                check = int(x[int(x[i+1]) + relative_base])
            
            if check == 0:
                if x[i][1] == '0':
                    i = int(x[int(x[i+2])])

                elif x[i][1] == '1':
                    i = int(x[i+2])
                
                elif x[i][1] == '2':
                    i = int(x[int(x[i+2]) + relative_base])

            else: 
                i += 3

        elif x[i][3:] == '07':
            if x[i][2] == '0':
                first_number = int(x[int(x[i+1])])
            
            elif x[i][2] == '1':
                first_number = int(x[i+1])
            
            elif x[i][2] == '2':
                first_number = int(x[int(x[i+1]) + relative_base])
            
            if x[i][1] == '0':
                second_number = int(x[int(x[i+2])])
            
            elif x[i][1] == '1': 
                second_number = int(x[i+2])
            
            elif x[i][1] == '2':
                second_number = int(x[int(x[i+2]) + relative_base])
            
            if first_number < second_number:
                if x[i][0] == '0':
                    x[int(x[i+3])] = '1'
                
                elif x[i][0] == '2':
                    x[int(x[i+3]) + relative_base] = '1'
            
            else:
                if x[i][0] == '0':
                    x[int(x[i+3])] = '0'
                
                elif x[i][0] == '2':
                    x[int(x[i+3]) + relative_base] = '0' 

            i += 4

        elif x[i][3:] == '08':    
            if x[i][2] == '0':
                first_number = int(x[int(x[i+1])])
            
            elif x[i][2] == '1': 
                first_number = int(x[i+1])
            
            elif x[i][2] == '2':
                first_number = int(x[int(x[i+1]) + relative_base])
            
            if x[i][1] == '0':
                second_number = int(x[int(x[i+2])])
            
            elif x[i][1] == '1': 
                second_number = int(x[i+2])
            
            elif x[i][1] == '2':
                second_number = int(x[int(x[i+2]) + relative_base])
            
            if first_number == second_number:
                if x[i][0] == '0':
                    x[int(x[i+3])] = '1'
                
                elif x[i][0] == '2':
                    x[int(x[i+3]) + relative_base] = '1'
            
            else:
                if x[i][0] == '0':
                    x[int(x[i+3])] = '0'
                
                elif x[i][0] == '2':
                    x[int(x[i+3]) + relative_base] = '0' 

            i += 4
        
        elif x[i][3:] == '09':
            if x[i][2] == '0':
                relative_base += int(x[int(x[i+1])])
            
            elif x[i][2] == '1':
                relative_base += int(x[i+1])
            
            elif x[i][2] == '2':
                relative_base += int(x[int(x[i+1]) + relative_base])
            
            i += 2


        elif x[i][3:] == '99':
            return False
            
        if output_count == 1:
            colour = output

        elif output_count == 2:
            direction = output
    
    return colour, direction, i

position = (0, 0)
direction = 0 # 0 is up, 1 is right, 2 is down, 3 is left
tiles_painted = set()
tile_colour = defaultdict(int) # initial colour of all tiles except first one are black, which is 0
tile_colour[position] = 1
state = True

while state:
    result = run_programme(tile_colour[position], i)
    if result == False:
        state = False
    
    else:
        colour_painted, direction_turn, i = result
        tile_colour[position] = colour_painted
        tiles_painted.add(position)

        if direction_turn == 0:
            direction += 3
        
        elif direction_turn == 1:
            direction += 1
                    
        if direction % 4 == 0:
            position = (position[0], position[1] - 1)
        
        elif direction % 4 == 1:
            position = (position[0] + 1, position[1])
        
        elif direction % 4 == 2:
            position = (position[0], position[1] + 1)
        
        elif direction % 4 == 3:
            position = (position[0] - 1, position[1])
        



coordinates_list = []
for i in range(45):
    for j in range(7):
        coordinates_list.append((i, j))

sorted_list = sorted(coordinates_list , key=lambda k: [k[1], k[0]])

for i in sorted_list:
    print(tile_colour[i], end='')    







