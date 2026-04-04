import pdb


grid = {}
with open("input.md", 'r', encoding='utf-8') as f:
    for line in f:
        line = line.split(" ")
        line[4] = line[4].strip("\n")
        #print(line)
        if line[0] not in grid:
            grid[line[0]] = {}
        if line[2] not in grid:
            grid[line[2]] = {}
        grid[line[0]][line[2]] = line[4]
        grid[line[2]][line[0]] = line[4]


areas = []

evaluations = {}
for point in grid:
    areas.append(point)
distance = 0
areas2 = areas.copy()
#breakpoint()
for area in areas2:
    distance = 0
    areas = areas2.copy()
    current_location = area
    areas.remove(current_location)
    while len(areas) > 0:
        highest = None
        for location in areas:
            if highest == None or int(grid[current_location][location]) > int(grid[current_location][highest]):
                highest = location

        print(f"location chosen: {highest}")
        distance += int(grid[current_location][highest])
        current_location = highest
        areas.remove(current_location)
    evaluations[area] = distance
    #breakpoint()

final_start = None
for area in evaluations:
    if final_start == None or evaluations[area] > evaluations[final_start]:
        final_start = area
print(f"With a starting point of {final_start} the smallest path is {evaluations[final_start]}")


