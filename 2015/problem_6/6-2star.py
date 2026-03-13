#This was a rather trivial change after solving the initial problem. All I did
#was change the values assigned.
lights = [[False for i in range(1000)] for j in range(1000)]

with open("input.md", "r", encoding="utf-8") as f:
    for line in f:
        char_count = 0
        instruction = None
        for char in line:
            if char.isnumeric():
                instruction = line.split(f'{char}', 1)
                break
            char_count += 1
        components = line.split(" ")
        match instruction[0].strip():
            case 'toggle':
                components[3] = components[3].strip("\n")
                point_1 = components[1].split(',')
                point_2 = components[3].split(',')
                for x in range(int(point_1[0]), int(point_2[0])+1):
                    for y in range(int(point_1[1]), int(point_2[1])+1):
                        lights[x][y] +=2
            case 'turn on':
                components[4] = components[4].strip("\n")
                point_1 = components[2].split(',')
                point_2 = components[4].split(',')
                for x in range(int(point_1[0]), int(point_2[0])+1):
                    for y in range(int(point_1[1]), int(point_2[1])+1):
                        lights[x][y] += 1
            case 'turn off':
                components[4] = components[4].strip("\n")
                point_1 = components[2].split(',')
                point_2 = components[4].split(',')
                for x in range(int(point_1[0]), int(point_2[0])+1):
                    for y in range(int(point_1[1]), int(point_2[1])+1):
                        if (lights [x][y] != 0):
                            lights[x][y] -= 1

on_count = 0
for i in range(1000):
    for j in range(1000):
        on_count += lights[i][j]

print(f"The total brightness is: {on_count}.")
