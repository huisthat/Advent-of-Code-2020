result=0
with open("day1.txt") as file:
	for line in file:
		number = int(line)
		number = number//3
		number = number-2
		result = result + number

		while number > 0:
			number = number // 3
			number = number - 2

			if number < 0:
				result = result
				
			else:
				result = result + number

print(result)

		

