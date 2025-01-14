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

def check_equation(numbers):
    result = numbers[0]

    list_result = []
    list_result.append(numbers[1] + numbers[2])
    list_result.append(numbers[1] * numbers[2])
    list_result.append(int(str(numbers[1]) + str(numbers[2])))

    for number in numbers[3:]:
        list_mem = []
        for r in list_result:
            list_mem.append(r + number)
            list_mem.append(r * number)
            list_mem.append(int(str(r) + str(number)))

        list_result = list_mem

    #print(list_result)
    for r in list_result:
        if r == result:
            return r
   
    return 0

result = 0

for equation in equations:
    result += check_equation(equation)
    #break

print(result)