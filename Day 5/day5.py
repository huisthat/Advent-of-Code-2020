
input_number = input("Input: ")

with open("day5.txt") as f:
	line = f.read()
	x = line.split(',')
	# for i in x:
	# 	x[i] = int(x[i])

i = 0
while True:
    x[i] = str(x[i])
    while len(x[i]) < 5:
        x[i] = '0' + x[i]

    if x[i][3:] == '01':
        if x[i][2] == '0':
            first_number = int(x[int(x[i+1])])
        
        else: 
            first_number = int(x[i+1])
        
        if x[i][1] == '0':
            second_number = int(x[int(x[i+2])])
        
        else: 
            second_number = int(x[i+2])

        index_to_replace = int(x[i+3])
        x[index_to_replace] = first_number + second_number
        i += 4

    elif x[i][3:] == '02': 
        if x[i][2] == '0':
            first_number = int(x[int(x[i+1])])
        
        else: 
            first_number = int(x[i+1])
        
        if x[i][1] == '0':
            second_number = int(x[int(x[i+2])])
        
        else: 
            second_number = int(x[i+2])

        index_to_replace = int(x[i+3])
        x[index_to_replace] = first_number * second_number
        i += 4

    elif x[i][3:] == '03':
        x[int(x[i+1])] = str(input_number)
        i += 2

    elif x[i][3:] == '04':
        if x[i][2] == '0':
            print(int(x[int(x[i+1])]))
        else:
            print(int(x[i+1]))
        i += 2
    
    elif x[i][3:] == '05':
        if x[i][2] == '0':
            check = int(x[int(x[i+1])])
        
        else: 
            check = int(x[i+1])
        
        if check != 0:
            if x[i][1] == '0':
                i = int(x[int(x[i+2])])

            else: 
                i = int(x[i+2])

        else: 
            i += 3

    elif x[i][3:] == '06':
        if x[i][2] == '0':
            check = int(x[int(x[i+1])])
        
        else: 
            check = int(x[i+1])
        
        if check == 0:
            if x[i][1] == '0':
                i = int(x[int(x[i+2])])

            else: 
                i = int(x[i+2])

        else: 
            i += 3

    elif x[i][3:] == '07':
        if x[i][2] == '0':
            first_number = int(x[int(x[i+1])])
        
        else: 
            first_number = int(x[i+1])
        
        if x[i][1] == '0':
            second_number = int(x[int(x[i+2])])
        
        else: 
            second_number = int(x[i+2])
        
        if first_number < second_number:
            x[int(x[i+3])] = '1'
        
        else:
            x[int(x[i+3])] = '0'
        
        i += 4

    elif x[i][3:] == '08':    
        if x[i][2] == '0':
            first_number = int(x[int(x[i+1])])
        
        else: 
            first_number = int(x[i+1])
        
        if x[i][1] == '0':
            second_number = int(x[int(x[i+2])])
        
        else: 
            second_number = int(x[i+2])
        
        if first_number == second_number:
            x[int(x[i+3])] = '1'
        
        else:
            x[int(x[i+3])] = '0'

        i += 4

    elif x[i][3:] == '99':
        break








