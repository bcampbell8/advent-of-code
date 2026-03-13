#Here I think i can employ the use of bitwise operators

#Need to intialise the array since its made of lists.
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
            #The end points of each range when making changes to light grid
            #gets an extra one added to it because it was stopping at the final
            #row of lights due to the end range being the limit.
            #How did i trouble shoot this? I set wrote after the assignment of
            #a block of lights was complete (one line in the input) I then
            #printed out all the lights turned on thus far and realised it
            #stopped one short for both x and y.
            case 'toggle':
                count = 0
                components[3] = components[3].strip("\n")
                point_1 = components[1].split(',')
                point_2 = components[3].split(',')
                for x in range(int(point_1[0]), int(point_2[0])+1):
                    for y in range(int(point_1[1]), int(point_2[1])+1):
                        lights[x][y] = not lights[x][y]
                        count +=1
            case 'turn on':
                components[4] = components[4].strip("\n")
                point_1 = components[2].split(',')
                point_2 = components[4].split(',')
                for x in range(int(point_1[0]), int(point_2[0])+1):
                    for y in range(int(point_1[1]), int(point_2[1])+1):
                        lights[x][y] = True
            case 'turn off':
                components[4] = components[4].strip("\n")
                point_1 = components[2].split(',')
                point_2 = components[4].split(',')
                for x in range(int(point_1[0]), int(point_2[0])+1):
                    for y in range(int(point_1[1]), int(point_2[1])+1):
                        lights[x][y] = False

on_count = 0
for i in range(1000):
    for j in range(1000):
        if lights[i][j] == True:
            on_count += 1

print(f"There are {on_count} lights on.")
