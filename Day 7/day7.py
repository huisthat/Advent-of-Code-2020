
import itertools
import copy

with open("day7.txt") as f:
	line = f.read()
	y = line.split(',')

y1 = copy.deepcopy(y)
y2 = copy.deepcopy(y)
y3 = copy.deepcopy(y)
y4 = copy.deepcopy(y)
y5 = copy.deepcopy(y)


def amplifier(x, input_signal, phase_setting):
    i = 0
    value = phase_setting
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
            x[int(x[i+1])] = str(value)
            value = input_signal
            i += 2

        elif x[i][3:] == '04':
            if x[i][2] == '0':
                output = int(x[int(x[i+1])])
            else:
                output = int(x[i+1])
            i += 2
            return x, i, output
        
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
            return False

def subsequent_amplifier(x, i, input_signal):
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
            x[int(x[i+1])] = str(input_signal)
            i += 2

        elif x[i][3:] == '04':
            if x[i][2] == '0':
                output = int(x[int(x[i+1])])
            else:
                output = int(x[i+1])
            i += 2
            return x, i, output
        
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
            return False, False, False

phases = [5, 6, 7, 8, 9]
possibilities = list(itertools.permutations(phases))

max_signal = 0

for phase in possibilities:

    x1, i1, amplifier_1 = amplifier(y1, 0, phase[0])
    x2, i2, amplifier_2 = amplifier(y2, amplifier_1, phase[1])
    x3, i3, amplifier_3 = amplifier(y3, amplifier_2, phase[2])
    x4, i4, amplifier_4 = amplifier(y4, amplifier_3, phase[3])
    x5, i5, amplifier_5 = amplifier(y5, amplifier_4, phase[4])

    while True: 
        x1, i1, amplifier_1 = subsequent_amplifier(x1, i1, amplifier_5)
        if amplifier_1 == False:
            break
        x2, i2, amplifier_2 = subsequent_amplifier(x2, i2, amplifier_1)
        if amplifier_2 == False:
            break
        x3, i3, amplifier_3 = subsequent_amplifier(x3, i3, amplifier_2)
        if amplifier_3 == False: 
            break
        x4, i4, amplifier_4 = subsequent_amplifier(x4, i4, amplifier_3)
        if amplifier_4 == False:
            break
        x5, i5, amplifier_5 = subsequent_amplifier(x5, i5, amplifier_4)
        if amplifier_5 == False:
            break

        signal = amplifier_5
        # print(signal)

        
    if amplifier_5 > max_signal:
        max_signal = amplifier_5


print(max_signal)




