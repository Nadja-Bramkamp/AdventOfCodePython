file = open("day1.txt", "r")

# Extract lists
list_left = []
list_right = []

for line in file:
    splitted = line.split(" ")
    list_left.append(int(splitted[0]))
    list_right.append(int(splitted[-1]))

# Calculate result
result = 0

for n in list_left:
    result += n * list_right.count(n)

print(result)
