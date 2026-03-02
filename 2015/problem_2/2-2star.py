#Ribbon length per present is equal to perimeter of smallest face

ribbon = 0
with open("input.md", "r", encoding="utf-8") as f:
    for line in f:
        present = line.rstrip().split("x")
        present[0] = int(present[0])
        present[1] = int(present[1])
        present[2] = int(present[2])
        #Sort list to give smallest two sides to calculate perimeter
        present.sort()
        ribbon += present[0] * present[1] * present[2] + present[0] * 2 + present[1] * 2

print(ribbon)
