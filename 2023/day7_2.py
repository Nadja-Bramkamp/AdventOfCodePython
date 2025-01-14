import numpy as np

#A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2
comparison = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, 'T': 8, 'J': -1, 'Q': 10, 'K': 11, 'A': 12}

# Get the type of the hand
def get_type(hand):
    # Count all occurences
    counts = []

    counts_J = hand.count('J')
    for key in comparison:
        if (key == 'J'):
            continue
        counts.append(hand.count(key))

    index_max =  np.argmax(counts)
    if (index_max.is_integer):
        counts[index_max] += counts_J
    else:
        counts[index_max[0]] += counts_J

    # Determine type
    if 5 in counts:
        return 6
    if 4 in counts:
        return 5
    if (3 in counts) and (2 in counts):
        return 4
    if 3 in counts:
        return 3
    if counts.count(2) == 2:
        return 2
    if 2 in counts:
        return 1
    return 0

# Compare hands: 
# 0 hand 1 is stronger
# 1 hand 2 is stringer
def compare_hands(hand1, hand2):
    type1 = get_type(hand1)
    type2 = get_type(hand2)

    if(type1 > type2):
        return 0
    if (type1 < type2):
        return 1
    
    for i in range(len(hand1)):
        if comparison[hand1[i]] > comparison[hand2[i]]:
            return 0
        if comparison[hand1[i]] < comparison[hand2[i]]:
            return 1


# Extract hands and bids
file = open("day7.txt", "r")

hands = []
bids = []

for line in file:
    if not line[-1].isdigit():
        line = line[:-1]
    substrings = line.split(' ')
    print(substrings)
    hands.append(substrings[0])
    bids.append(int(substrings[1]))

# Calculate result
result = 0

for i in range(len(hands)):
    count_lower = 1
    for h in hands:
        if (hands[i] == h):
            continue
        if compare_hands(hands[i], h) == 0:
            count_lower += 1
    result += count_lower * bids[i]

print(result)