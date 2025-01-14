def find_x(lines):
    result = 0

    for i in range(len(lines[0]) - 2):
        substring1 = lines[0][i : i+3]
        substring2 = lines[1][i : i+3]
        substring3 = lines[2][i : i+3]

        if (substring2[1] != 'A'):
            continue

        if ((substring1[0] == 'M' and substring3[2] == 'S') or (substring1[0] == 'S' and substring3[2] == 'M')):
            if ((substring3[0] == 'M' and substring1[2] == 'S') or (substring3[0] == 'S' and substring1[2] == 'M')):
                result += 1

    return result


file = open("day4.txt", "r")
file = file.readlines()

file[-1] = file[-1] + '\n'

result = 0

for i in range(len(file) - 2):
    result += find_x(file[i : i+3])
    
print(result)
