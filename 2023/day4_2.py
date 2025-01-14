import re

def next_cards(line, start_card):
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
    result = []

    for w in winning_numbers:
        if w in numbers:
            start_card += 1
            result.append(start_card)

    return result


file = open("day4.txt", "r")
file = file.readlines()

copies = []

for i in range(len(file)):
    cards = next_cards(file[i], i + 1)
    copies += cards

originals = len(file)

for c in copies:
    copies += next_cards(file[c - 1], c)

print(originals + len(copies))