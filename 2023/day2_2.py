def power(line):
    #Get the relevant line part
    start_index = line.index(":")
    line = line[(start_index + 1):]

    # Store number of cubes
    cubes_dict = {"red": 0, "blue": 0, "green": 0}

    # Get subsets
    subsets = line.split("; ")

    # Update max number of cubes
    for s in subsets:
        cubes = s.split(", ")
        for c in cubes:
            for color in cubes_dict:
                if color in c:
                    update_dict(c, color, cubes_dict)

    # Return power
    return cubes_dict["red"] * cubes_dict["blue"] * cubes_dict["green"]

            
# Update dictionary if greater number of cubes is needed
def update_dict(cube, color, dict):
    index = cube.find(color)
    number_cubes = int(cube[:(index - 1)])
    if (dict[color] < number_cubes):
        dict[color] = number_cubes



file = open("day2.txt", "r")

result = 0

for line in file:
    result += power(line)

print(result)