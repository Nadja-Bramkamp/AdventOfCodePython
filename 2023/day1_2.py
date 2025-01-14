def calibration_value(line):
    first_digit = 0
    last_digit = 0

    index_first_digit = len(line)
    index_last_digit = len(line)
    
    # Check for numbers substring
    numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    # First digit
    for k in numbers:
        index = line.find(k)
        if index == -1:
            continue
        if index < index_first_digit:
            index_first_digit = index
            first_digit = numbers[k]

    # Last digit
    # Reverse the strings 
    reversed_line = line[::-1]
    for k in numbers:
        index = reversed_line.find(k[::-1])
        if index == -1:
            continue
        #index -= 1
        # Get index in reverse string
        if index < index_last_digit:
            index_last_digit = index
            last_digit = numbers[k]

    # First digit
    for i in range(index_first_digit):
        if line[i].isdigit():
            first_digit = int(line[i])
            break
    
    # Last digit
    for i in range(index_last_digit):
        if reversed_line[i].isdigit():
            last_digit = int(reversed_line[i])
            break

    # Return result
    return first_digit * 10 + last_digit

#print(calibration_value("4nineeightseven2"))

# Read in file
file = open("day1.txt", mode="r")

# Store result
result = 0

for line in file:
    result += calibration_value(line)

file.close()
print(result)