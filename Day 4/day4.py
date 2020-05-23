count = 0

def is_valid(number):
    digit = [int(i) for i in str(number)]
    for i in range(5):
        if digit[i+1] < digit[i]:
            return False
    
    digit_count = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
    for i in range(5):
        if digit[i] == digit[i+1]:
            digit_count[str(digit[i])] += 1
    if 1 in digit_count.values():
        return True
    return False

for password in range(124075 , 580770):
    if is_valid(password):
        count += 1

print(count)