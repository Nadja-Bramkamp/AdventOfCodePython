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
    #if k != "0":
    #    continue
    positions = dict[k]
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            x_1, y_1 = positions[i]
            x_2, y_2 = positions[j]

            #print(x_1, y_1)
            #print(x_2, y_2)

            # Calculate differences
            diff_x = x_1 - x_2
            diff_y = y_1 - y_2

            # Calculate position of antinode 1
            antinode_x = x_1 + diff_x
            antinode_y = y_1 + diff_y

            if antinode_x < len(map) and antinode_x >= 0 and antinode_y < len(map[-1]) and antinode_y >= 0:
                if (not (antinode_x, antinode_y) in result):
                    result.append((antinode_x, antinode_y))
                #print(antinode_x, antinode_y)
                #if map[antinode_x][antinode_y] == ".":
                #    map[antinode_x] = map[antinode_x][:antinode_y] + "#" + map[antinode_x][antinode_y + 1:]
                #    result += 1
                #elif map[antinode_x][antinode_y] != "#":
                #    result += 1

            # Calculate position of antinode 2
            antinode_x = x_2 - diff_x
            antinode_y = y_2 - diff_y

            if antinode_x < len(map) and antinode_x >= 0 and antinode_y < len(map[-1]) and antinode_y >= 0:
                if (not (antinode_x, antinode_y) in result):
                    result.append((antinode_x, antinode_y))
                #print(antinode_x, antinode_y)
                #if map[antinode_x][antinode_y] == ".":
                #    map[antinode_x] = map[antinode_x][:antinode_y] + "#" + map[antinode_x][antinode_y + 1:]
                #    result += 1
                #elif map[antinode_x][antinode_y] != "#":
                #    result += 1

            #print("")

#for line in map:
#    result += line.count("#")

print(result)
print(len(result))

#for line in map[:-1]:
#    print(line[:-1])

#print(map[-1])