
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
x = len(layer_list)
print(layer_list)

final_layer = []
for i in layer_list[0]:
    final_layer.append(i)

print(final_layer)


for i in range(len(final_layer)):
    if final_layer[i] == 0 or final_layer[i] == 1:
        pass
    elif final_layer[i] == 2:
        for number in range(len(layer_list)):
            y = layer_list[number][i]
            if y == 0 or y == 1:
                final_layer[i] = y 
                # print(final_layer[i])
                break
            else: 
                pass

print(final_layer)


