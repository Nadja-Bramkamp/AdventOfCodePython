import re

def count_points(line):
    # Split into string of winning numbers and numbers
    substring = re.split("[:|\n]", line)
    winning_numbers = substring[1]
    numbers = substring[2]

    # Convert numbers to lists
    winning_numbers = winning_numbers.split(" ")
    numbers = numbers.split(" ")

    winning_numbers = [w for w in winning_numbers if w != '']
    numbers = [n for n in numbers if n != '']

    # Calculate results
    result = 0

    for w in winning_numbers:
        if w in numbers:
            if result == 0:
                result = 1
            else:
                result *= 2

    return result


file = open("day4.txt", "r")

result = 0

for line in file:
    result += count_points(line)

print(result)