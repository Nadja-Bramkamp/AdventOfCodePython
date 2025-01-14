import pandas as pd

file = open("day5.txt", "r")
file = file.readlines()

# Extract seeds
seeds = file[0][7:-1]
seeds = seeds.split(' ')
seeds = [int(s) for s in seeds]

# Extract the mappings
mappings = []

current_mapping = []
for i in range(2, len(file) - 1):
    if (file[i] == '\n'):
        mappings.append(current_mapping)
        current_mapping = []
        continue
    list = file[i][:-1].split(' ')
    if (len(list) == 2):
        continue
    list = [int(x) for x in list]
    current_mapping.append(list)

list = file[len(file) - 1].split(' ')
list = [int(x) for x in list]
current_mapping.append(list)
mappings.append(current_mapping)

def calculate_mapping(mapping, input):
    for m in mapping:
        dest = m[0]
        source = m[1]
        r = m[2]

        if (input >= source and input < source + r):
            diff = input - source
            return dest + diff
    return input

locations = []

for s in seeds:
    input = s
    for mapping in mappings:
        input = calculate_mapping(mapping, input)
    locations.append(input)

print(min(locations))