import re

file = open("day3.txt", "r")

result = 0

do = 1

for line in file:
    print(line)
    matches = [x.group() for x in re.finditer(pattern="mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)", string=line)]
    for m in matches:
        if (m == "do()"):
            do = 1
        elif (m == "don't()"):
            do = 0
        else:
            index_split = m.find(",")
            factor1 = m[4:index_split]
            factor2 = m[(index_split + 1):-1]
            result += do * int(factor1) * int(factor2)

print(result)