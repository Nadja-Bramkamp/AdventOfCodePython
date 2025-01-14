file = open("day8.txt", "r")
file = file.readlines()

input = file[0][:-1]

dict = {}

# Create dictionary with left / right
for i in range(2, len(file)):
    node = file[i][:3]

    left = file[i][7:10]
    right = file[i][12:15]

    dict[node] = [left, right]

# Determine start nodes
start_nodes = []

for key in dict:
    if key[2] == "A":
        start_nodes.append(key)

print(start_nodes)

j = 0
input_length = len(input)

while(True):
    direction = input[j % input_length]

    if (direction == "L"):
        for k in range(len(start_nodes)):
            start_nodes[k] = dict[start_nodes[k]][0]
    if (direction == "R"):
        for k in range(len(start_nodes)):
            start_nodes[k] = dict[start_nodes[k]][1]

    j += 1
    
    complete = True
    for n in start_nodes:
        if (n[2] != "Z"):
            complete = False
            break
    if complete:
        break

        
print(j)
