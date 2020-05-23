with open("day2.txt") as f:
	line = f.read()
	x = line.split(',')
	# for i in range(len(x)):
	for i, item in enumerate(x):
		x[i] = int(x[i])

# for noun in range(100):
# x[1] = noun
# for verb in range(100):
# 	x[2] = verb

def f(y,z):

	i = 0
	x[1] = y
	x[2] = z
	while True:

		if x[i] == 1:
			index_to_replace = x[i+3]
			x[index_to_replace] = x[x[i+1]] + x[x[i+2]]
			i = i + 4
		elif x[i] == 2: 
			index_to_replace = x[i+3]
			x[index_to_replace] = x[x[i+1]] * x[x[i+2]]
			i = i + 4
		elif x[i] == 99:
			break
	return x[0]

# output = f(y,z)
for noun in range(100):
	for verb in range(100):
		output = f(noun,verb)
		if output == 19690720:
			print(noun,verb)
		





