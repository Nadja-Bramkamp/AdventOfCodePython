import re

file = open("day3.txt", "r")

result = 0

for line in file:
    print(line)
    matches = re.findall(pattern="mul\((\d{1,3}),(\d{1,3})\)", string=line)
    for m in matches:
        result += int(m[0]) * int(m[1])

print(result)