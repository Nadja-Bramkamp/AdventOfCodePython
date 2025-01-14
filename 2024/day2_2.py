def remove_levels(line):
    for i in range(len(line)):
        numbers = line[:i] + line[i + 1:]
        #print(numbers)
        if (numbers[0] <= numbers[1]): #Increasing
            for i in range(len(numbers) - 1):
                diff = numbers[i + 1] - numbers[i]
                if (diff < 1 or diff > 3):
                    break
                if i == (len(numbers) - 2):
                    return 1
            
        else: #Decreasing
            for i in range(len(numbers) - 1):
                diff = numbers[i] - numbers[i + 1]
                if (diff < 1 or diff > 3):
                    break
                if i == (len(numbers) - 2):
                    return 1
    return 0

file = open("day2.txt", "r")

result = 0

for line in file:
    numbers = line.split(" ")
    numbers = [int(n) for n in numbers]
    result += remove_levels(numbers)

print(result)