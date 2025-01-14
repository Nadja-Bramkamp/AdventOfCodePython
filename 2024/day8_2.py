# Read in map
map = open("day8.txt", "r")
map = map.readlines()

# Store antenna locations
dict = {}

for i in range(len(map)):
    for j in range(len(map[i])):
        c = map[i][j]
        if c != '\n' and c != '.':
            if c in dict.keys():
                dict[c].append((i, j))
            else:
                dict[c] = [(i, j)]

# Calculate result
result = []

# Calculate the locations of the antinodes
for k in dict.keys():
    if k == "#":
        continue
    positions = dict[k]
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            x_1, y_1 = positions[i]
            x_2, y_2 = positions[j]

            # Calculate differences
            diff_x = x_1 - x_2
            diff_y = y_1 - y_2

            # Calculate position of antinode 1
            antinode_x = x_1 + diff_x
            antinode_y = y_1 + diff_y

            if antinode_x < len(map) and antinode_x >= 0 and antinode_y < len(map[-1]) and antinode_y >= 0:
                if (not (antinode_x, antinode_y) in result):
                    result.append((antinode_x, antinode_y))

            # Calculate position of antinode 2
            antinode_x = x_2 - diff_x
            antinode_y = y_2 - diff_y

            if antinode_x < len(map) and antinode_x >= 0 and antinode_y < len(map[-1]) and antinode_y >= 0:
                if (not (antinode_x, antinode_y) in result):
                    result.append((antinode_x, antinode_y))

print(len(result))
result_x = []
result_y = []

for r in result:
    result_x.append(r[0])
    result_y.append(r[1])

for k in dict.keys():
    for p in dict[k]:
        if (p[0] in result_x or p[1] in result_y) and (p not in result):
            result.append(p)


#print(result)
print(len(result))
