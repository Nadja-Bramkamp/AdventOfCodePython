file = open("day1.txt", "r")

# Extract lists
list_left = []
list_right = []

for line in file:
    splitted = line.split(" ")
    list_left.append(int(splitted[0]))
    list_right.append(int(splitted[-1]))

# Sort lists
list_left.sort()
list_right.sort()

#Calculate result
result = 0

for i in range(len(list_left)):
    result += abs(list_left[i] - list_right[i])

print(result)