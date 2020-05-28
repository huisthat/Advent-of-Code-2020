
from itertools import islice

number_list = []
with open("day8.txt") as file:
    image = file.read()
    for number in image:
        number_list.append(int(number))


# print(len(number_list))

def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())

layer_list = list(chunk(number_list, 25*6))
print(layer_list)

def count_zero(layer):
    zero = 0
    for i in layer:
        if i == 0:
            zero += 1
    return zero

def count_one(layer):
    one = 0
    for i in layer:
        if i == 1:
            one += 1
    return one

def count_two(layer):
    two = 0
    for i in layer:
        if i == 2:
            two += 1
    return two


min_zero = count_zero(layer_list[0])
for layer in layer_list:
    if count_zero(layer) < min_zero:
        min_zero = count_zero(layer)

for layer in layer_list:
    if count_zero(layer) == min_zero:
        number = count_one(layer) * count_two(layer)
    
print(number)

