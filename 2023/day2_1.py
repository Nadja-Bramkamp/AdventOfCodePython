def possible_game(line):
    #Get the Game ID
    start_index = line.index("Game ")
    end_index = line.index(":")
    id = line[(start_index + 5): end_index]
    id = int(id)

    # Define number of cubes
    red_cubes = 12
    blue_cubes = 14
    green_cubes = 13

    # Get subsets
    subsets = line[(end_index + 2):].split("; ")

    # Check numbers
    for s in subsets:
        cubes = s.split(", ")
        for c in cubes:
            if not (check_numbers(c, "red", red_cubes) and check_numbers(c, "blue", blue_cubes) 
                and check_numbers(c, "green", green_cubes)):
                return 0
    return id
            
# Return true if the number of cubes is less than definied
def check_numbers(cube, color, max_number):
    index = cube.find(color)
    if index == -1:
        return True
    if (int(cube[:(index - 1)]) <= max_number):
        return True
    return False




file = open("day2.txt", "r")

result = 0

for line in file:
    result += possible_game(line)

print(result)