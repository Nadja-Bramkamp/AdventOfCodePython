file = open("day6.txt", "r")

file = file.readlines()

#Time
time = file[0]
time = time[5:-1]
time = time.split(' ')
time = [t for t in time if len(t) > 0]
duration = ""
for t in time:
    duration += t

duration = int(duration)

#Distance
distance = file[1]
distance = distance[9:]
distance = distance.split(' ')
distance = [d for d in distance if len(d) > 0]

length = ""
for d in distance:
    length += d
length = int(length)


result = 0

for i in range(duration + 1):
    if (i * (duration - i)) > length:
        result += 1

print(result)
