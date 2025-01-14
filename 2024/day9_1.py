file = open("day9.txt", "r")
file = file.readlines()
file = file[0]

def convert_string(file):
    id = 0
    block = 1
    result = ""

    for i in range(len(file)):
        c = int(file[i])
        if block == 1:
            result += str(id) * int(c)
            id += 1
            block = 0
        else:
            result += "." * int(c)
            block = 1
    return result

def reorder(string):
    index_1 = 0
    index_2 = len(string) - 1

    while (index_1 < index_2):
        if (string[index_1] != "."):
            index_1 += 1
        else:
            while string[index_2] == ".":
                index_2 -= 1
            string = string[:index_1] + string[index_2] + string[index_1 + 1:]
            string = string[:index_2] + "." + string[index_2 + 1:]
            index_1 += 1
    return string

def calculate_checksum(string):
    result = 0
    for i in range(len(string)):
        if string[i] == ".":
            break
        result += i * int(string[i])
    return result

convert = convert_string(file)
reordered = reorder(convert)
checksum = calculate_checksum(reordered)

print(checksum)
