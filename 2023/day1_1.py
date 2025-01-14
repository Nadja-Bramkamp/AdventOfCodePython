def calibration_value(line):
    first_digit = 0
    last_digit = 0

    # First digit
    for c in line:
        if c.isdigit():
            first_digit = int(c)
            break
    
    # Last digit
    reversed_line = line[::-1]
    for c in reversed_line:
        if c.isdigit():
            last_digit = int(c)
            break

    # Return result
    return first_digit * 10 + last_digit

# Read in file
file = open("day1.txt", mode="r")

# Store result
result = 0

for line in file:
    result += calibration_value(line)

file.close()
print(result)