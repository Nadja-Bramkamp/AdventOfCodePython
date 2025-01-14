import re

def get_adjacent_numbers(before, current, next):
    # Get symbol indices of line before
    indices_before = get_symbol_indices(before)

    # Get symbol indices of next line
    indices_next = get_symbol_indices(next)

    # Get symbol indices of current line
    indices_current = get_symbol_indices(current)

    # Merge all indices
    indices = indices_before + indices_next + indices_current

    # Store result
    result = 0

    # Get numbers in current line
    for match in re.finditer(r'(\d+)', current):
        print(match.start())
        print(match.end())
        for i in range(match.start() - 1, match.end() + 1):
            if i in indices:
                result += int(current[match.start() : match.end()])
                print(int(current[match.start() : match.end()]))
                break
    
    return result

def get_symbol_indices(line):
    indices = []
    if line != None:
        for i in range(len(line)):
            if ((line[i] != ".") and not line[i].isdigit()):
                indices.append(i)
    return indices

file = open("test.txt", "r")
file = file.readlines()

result = get_adjacent_numbers(None, file[0], file[1]) 

for i in range(1, len(file) - 1):
    result += get_adjacent_numbers(file[i - 1], file[i], file[i + 1])

result += get_adjacent_numbers(file[-2], file[-1], None)

print(result)