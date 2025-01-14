file = open("day6.txt", "r")

file = file.readlines()

#Time
time = file[0]
time = time[5:-1]
time = time.split(' ')
time = [int(t) for t in time if len(t) > 0]

#Distance
distance = file[1]
distance = distance[9:]
distance = distance.split(' ')
distance = [int(d) for d in distance if len(d) > 0]

#Calculate result
r = 1

def calculate_ways(time, distance):
    result = 0

    for i in range(time + 1):
        #print(i * (time - i))
        if (i * (time - i)) > distance:
            result += 1

    return result

for i in range(len(time)):
    t = time[i]
    d = distance[i]

    # Calculate number of ways
    r *= calculate_ways(t, d)

print(r)