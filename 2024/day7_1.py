import re

# Read in file
file = open("day7.txt", "r")

# Extract numbers
equations = []

for line in file:
    numbers = re.split(": | |\n", line)
    if numbers[-1] == '':
        numbers = numbers[:-1]
    numbers = [int(n) for n in numbers]
    equations.append(numbers)

# Function to check equation
# Iteration 1: 0, 1
# Iteration 2: 2, 3, 4, 5
# Iteration 3: 6, 7, 8, 9, 10, 11, 12, 13 
def check_equation(numbers):
    result = numbers[0]

    list_result = []
    list_result.append(numbers[1] + numbers[2])
    list_result.append(numbers[1] * numbers[2])

    for number in numbers[3:]:
        list_mem = []
        for r in list_result:
            list_mem.append(r + number)
            list_mem.append(r * number)

        list_result = list_mem

    for r in list_result:
        if r == result:
            return r
   
    return 0

result = 0

for equation in equations:
    result += check_equation(equation)

print(result)