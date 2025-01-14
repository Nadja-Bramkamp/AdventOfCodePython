def horizontal(line):
    result = 0
    result += line.count("XMAS")
    result += line.count("SAMX")
    return result

def vertical(lines):
    result = 0

    #Create vertical strings and check 
    for i in range(len(lines[0])):
        str = ""
        for line in lines:
            str += line[i]
        if (str == "XMAS" or str == "SAMX"):
            print("vertical")
            result += 1

    return result

def diagonal(lines):
    result = 0

    # Left shift
    left_lines = []
    index = 0

    # Create shifted lines
    for line in lines:
        left_lines.append(line[-index:-1] + "-" + line[:-index])
        index += 1

    result += vertical(left_lines)

    # Right shift
    right_lines = []
    index = 0

    # Create shifted lines
    for line in lines:
        right_lines.append(line[index:-1] + "-" + line[:index])
        index += 1

    result += vertical(right_lines)

    return result

file = open("day4.txt", "r")
file = file.readlines()

file[-1] = file[-1] + '\n'

result = 0

for i in range(len(file)):
    # Horizontal
    result += horizontal(file[i])

    # Vertical and diagonal with following lines
    end_line = i + 4
    if (end_line <= len(file)):
        print(end_line)
        result += vertical(file[i:end_line])
        result += diagonal(file[i:end_line])
    #print(i)
    #print(end_line)
    
print(result)
