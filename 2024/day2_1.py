def check_line(line):
    numbers = line.split(" ")
    numbers = [int(n) for n in numbers]

    if (numbers[0] <= numbers[1]): #Increasing
        for i in range(len(numbers) - 1):
            diff = numbers[i + 1] - numbers[i]
            if (diff < 1 or diff > 3):
                return 0
    else: #Decreasing
        for i in range(len(numbers) - 1):
            diff = numbers[i] - numbers[i + 1]
            if (diff < 1 or diff > 3):
                return 0
    return 1

file = open("day2.txt", "r")

result = 0

for line in file:
    result += check_line(line)

print(result)