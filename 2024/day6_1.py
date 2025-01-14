# Read in map
file = open("day6.txt", "r")
file = file.readlines()

# Remove \n
for i in range(len(file) - 1):
    file[i] = file[i][:-1]

# Get position of ^
row = 0
col = 0
while row < len(file):
    if file[row].find("^") > -1:
        col = file[row].find("^")
        break
    row += 1

# direction 0: up, 1: right, 2: down, 3: left
direction = 0

# Move through map
while True:
    next_row = -1
    next_col = -1
    # Determine next row and col
    if direction == 0: #up
        next_row = row - 1
        next_col = col
    elif direction == 1: #right
        next_row = row
        next_col = col + 1
    elif direction == 2: #down
        next_row = row + 1
        next_col = col
    else: #left
        next_row = row
        next_col = col - 1
    
    if not (next_row >= 0 and next_row < len(file) and next_col >= 0 and next_col < len(file[0])):
        break

    # Obstacle
    if (file[next_row][next_col] == "#"):
        direction = (direction + 1) % 4
    else:
        file[row] = file[row][:col] + "X" + file[row][col + 1:]
        row = next_row
        col = next_col

# Count X
result = 1

for i in range(len(file)):
    result += file[i].count("X")

print(result)
