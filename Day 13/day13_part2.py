
from collections import defaultdict


with open("day13.txt") as f:
	line = f.read()
	initial_list = line.split(',')


x = defaultdict(int)

for count, item in enumerate(initial_list):
    x[count] = item

x[0] = '2'

i = 0
relative_base = 0

def intcode(i, relative_base, input_number):
    output = []
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
            if input_number is None:
                return output, i, relative_base

            if x[i][2] == '0':
                x[int(x[i+1])] = str(input_number)
            
            elif x[i][2] == '2':
                x[int(x[i+1]) + relative_base] = str(input_number)

            input_number = None
            i += 2

        elif x[i][3:] == '04':
            if x[i][2] == '0':
                output.append(int(x[int(x[i+1])]))

            elif x[i][2] == '1':
                output.append(int(x[i+1]))
            
            elif x[i][2] == '2':
                output.append(int(x[int(x[i+1]) + relative_base]))

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
            return False, output

            

input_number = None
# output = []
position = [None, None]

def find_tile_ball(input_number, i, relative_base):
    count = 0
    while True:
        result = intcode(i, relative_base, input_number)
        
        if result == False:
            return False

        number, i, relative_base = result

        for j in range(2, len(number), 3):

            if number[j] == 3:
                position[0] = number[j-2]
                count += 1
            
            elif number[j] == 4:
                position[1] = number[j-2]
                count += 1
            elif number[j-2] == -1 and number[j-1] == 0:
                print(number[j])
        
        if position[0] is not None and position[1] is not None:
            break

    print(position)
    return position, i, relative_base

paddle_x = None
ball_x = None

def get_paddle_x(outputs, x):
    for i in range(2, len(outputs), 3):
        if outputs[i] == 3:
            return outputs[i-2]
    return x

def get_ball_x(outputs, x):
    for i in range(2, len(outputs), 3):
        if outputs[i] == 4:
            return outputs[i-2]
    return x

def get_score(outputs):
    for i in range(2, len(outputs), 3):
        if outputs[i-2] == -1 and outputs[i-1] == 0:
            print("SCORE::::", outputs[i])

cnt = 0
while True:
    result = intcode(i, relative_base, input_number)
    if result[0] is False:
        get_score(result[1])
        break
    number, i, relative_base = result

    paddle_x = get_paddle_x(number, paddle_x)
    ball_x = get_ball_x(number, ball_x)
    # get_score(number)
    
    if ball_x is not None and paddle_x is not None:
        if ball_x > paddle_x:
            input_number = 1
        elif ball_x < paddle_x:
            input_number = -1
        else:
            input_number = 0

    if cnt < 10:
        print(paddle_x, ball_x)
        print(input_number)
        cnt += 1
    # blabla


# while True:
#     result = find_tile_ball(input_number, i, relative_base)

#     if result == False:
#         break
    
#     position, i, relative_base = result
#     if position[0] > position[1]:
#         input_number = -1
    
#     elif position[0] < position[1]:
#         input_number = 1
    
#     else:
#         input_number = 0


# for i in output:
#     if i[0] == -1 and i[1] == 0:
#         print(i[2])

