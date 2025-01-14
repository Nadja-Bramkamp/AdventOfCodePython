# Read in map
file = open("day6.txt", "r")
file = file.readlines()

# Remove \n
for i in range(len(file) - 1):
    file[i] = file[i][:-1]

# Move 
def move(file, row, col, direction):
    obstacles = []
    mark = ""
    # Move through map
    while True:
        next_row = -1
        next_col = -1
        # Determine next row and col
        if direction == 0: #up
            mark = "|"
            next_row = row - 1
            next_col = col
        elif direction == 1: #right
            mark = "-"
            next_row = row
            next_col = col + 1
        elif direction == 2: #down
            mark = "|"
            next_row = row + 1
            next_col = col
        else: #left
            mark = "-"
            next_row = row
            next_col = col - 1
        
        # Out of map
        if not (next_row >= 0 and next_row < len(file) and next_col >= 0 and next_col < len(file[0])):
            return 0


        # Obstacle
        if (file[next_row][next_col] == "#" or file[next_row][next_col] == "O"):
            for k in range(0, len(obstacles), 4):
                if obstacles[-k] == (next_row, next_col) and obstacles[-k-1] == obstacles[-1]:
                    return 1
 
            obstacles.append((next_row, next_col))
            file[row] = file[row][:col] + "+" + file[row][col + 1:]
            direction = (direction + 1) % 4
        else:
            if file[row][col] == ".":
                file[row] = file[row][:col] + mark + file[row][col + 1:]
            else:
                if (direction == 0 or direction == 2) and file[row][col] == "-":
                    file[row] = file[row][:col] + "+" + file[row][col + 1:]
                if (direction == 1 or direction == 3) and file[row][col] == "|":
                    file[row] = file[row][:col] + "+" + file[row][col + 1:]
            row = next_row
            col = next_col


# Get position of ^
row = 0
col = 0
while row < len(file):
    if file[row].find("^") > -1:
        col = file[row].find("^")
        break
    row += 1

# Brute force the new obstacle positions:
result = 0

for i in range(len(file)):
    for j in range(len(file[i])):
        if (file[i][j] == "."):
            file_copy = file.copy()
            file_copy[i] = file_copy[i][:j] + "O" + file_copy[i][j + 1:]
            m = move(file_copy, row, col, 0)
            result += m
            if m == 1:
                print(i, j)


print(result)
