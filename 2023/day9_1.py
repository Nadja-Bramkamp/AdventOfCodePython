import numpy as np

file = open("day9.txt", "r")
file = file.readlines()
file[-1] += '\n'

histories = []

for line in file:
    history = line.split(" ")
    history[-1] = history[-1][:-1]
    history = [int(h) for h in history]
    histories.append(history)

def calculate_derivatives(history):
    result = [history]

    while any(history):
        history = np.diff(history).tolist()
        result.insert(0, history)

    return result

def calculate_next(histories):
    history = histories[0]
    history.append(0)

    for i in range(1, len(histories)):
        histories[i].append(histories[i][-1] + histories[i - 1][-1])
    return histories[-1][-1]

# Calculate result
result = 0

for history in histories:
    deriv = calculate_derivatives(history)
    result += calculate_next(deriv)

print(result)