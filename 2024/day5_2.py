file = open("day5.txt", "r")
file = file.readlines()
# Simplyfing processing by adding \n
file[-1] += "\n"

i = 0

# Extract order rules
dict = {}

while file[i] != "\n":
    order_rule = file[i].split("|")
    first_page = int(order_rule[0])
    second_page = int(order_rule[1][:-1])
    if first_page in dict.keys():
        dict[first_page].append(second_page)
    else:
        dict[first_page] = [second_page]
    i += 1

i += 1

# Extract Updates
updates = []

for j in range(i, len(file)):
    update = file[j].split(",")
    update[-1] = update[-1][:-1]
    update = [int(u) for u in update]
    updates.append(update)

# Calculate the result
result = 0

def order_update(update, dict):
    for j in range(len(update)):
        page = update[j]
        for k in range(j + 1, len(update)):
            if update[k] not in dict.keys():
                continue
            if page in dict[update[k]]:
                update[j] = update[k]
                update[k] = page
                return order_update(update, dict)
    return update


for update in updates:
    correct_update = True
    for j in range(len(update)):
        page = update[j]
        for k in range(j + 1, len(update)):
            if update[k] not in dict.keys():
                break
            if page in dict[update[k]]:
                correct_update = False
                break
        if not correct_update:
            break
    if not correct_update:
        print(update)
        ordered = order_update(update, dict)
        print(ordered)
        result += ordered[len(ordered) // 2]

print(result)
