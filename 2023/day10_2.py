# Read in file
file = open("test.txt", "r")
file = file.readlines()

# Exclude \n
for i in range(len(file) - 1):
    file[i] = file[i][:-1]

# Find start position
start_position = (-1, -1)
for i in range(len(file)):
    for j in range(len(file[i])):
        if file[i][j].find("S") > -1:
            start_position = (i, j)
            break
    if (start_position != (-1, -1)):
        break

# direction: 0: up, 1: right, 2: down, 3:left
def move(file, direction, row, col):
    # North South Connection
    if file[row][col] == "|":
        if direction == 0:
            row -= 1
        if direction == 2:
            row += 1
    # East West Connection
    elif file[row][col] == "-":
        if direction == 1:
            col += 1
        if direction == 3:
            col -= 1
    # North East Connection
    elif file[row][col] == "L":
        if direction == 2:
            direction = 1
            col += 1
        if direction == 3:
            direction = 0
            row -= 1
    # North West Connection
    elif file[row][col] == "J":
        if direction == 2:
            direction = 3
            col -= 1
        if direction == 1:
            direction = 0
            row -= 1
    # South West Connection
    elif file[row][col] == "7":
        if direction == 0:
            direction = 3
            col -= 1
        if direction == 1:
            direction = 2
            row += 1
    # South East Connection
    elif file[row][col] == "F":
        if direction == 0:
            direction = 1
            col += 1
        if direction == 3:
            direction = 2
            row += 1
    return direction, row, col

# Get start directions
directions = -1
row = -1
col = -1

(start_row, start_col) = start_position

if start_row > 0:
    if file[start_row - 1][start_col] != ".":
        direction = 0
        row = start_row - 1
        col = start_col
if start_col < len(file[0]) - 1:
    if file[start_row][start_col + 1] != ".":
        direction = 1
        row = start_row
        col = start_col + 1
if start_row < (len(file) - 1):
    if file[start_row + 1][start_col] != ".":
        direction = 2
        row = start_row + 1
        col = start_col
if start_col > 0:
    if file[start_row][start_col - 1] != ".":
        direction = 3
        row = start_row
        col = start_col - 1

positions = [(row, col)]
result = 1
while True:
    direction, row, col = move(file, direction, row, col)
    positions.append((row, col))
    result += 1
    if row == start_position[0] and col == start_position[1] and result > 1:
        break
print(result // 2)
