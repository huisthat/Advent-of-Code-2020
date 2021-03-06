
from collections import defaultdict


with open("day13.txt") as f:
	line = f.read()
	initial_list = line.split(',')


x = defaultdict(int)

for count, item in enumerate(initial_list):
    x[count] = item


i = 0
relative_base = 0

def run_programme(i, relative_base):
    while True:
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
                x[int(x[i+1])] = str(input_number)
            
            elif x[i][2] == '2':
                x[int(x[i+1]) + relative_base] = str(input_number)
            i += 2

        elif x[i][3:] == '04':
            if x[i][2] == '0':
                output = int(x[int(x[i+1])])

            elif x[i][2] == '1':
                output = int(x[i+1])
            
            elif x[i][2] == '2':
                output = int(x[int(x[i+1]) + relative_base])

            i += 2
            return output, i, relative_base
        
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

output = []
while True: 
    result = run_programme(i, relative_base)
    
    if result == False:
        break
    
    number, i, relative_base = result
    output.append(number)

block_tiles = []
for i in range(2, len(output), 3):
    if output[i] == 2:
        block_tiles.append((output[i-2], output[i-1]))

print(len(block_tiles))