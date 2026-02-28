import pdb

f = open("input.txt", "r", encoding="utf-8")
instructions = f.read()
floor = 0
for x in instructions:
    match x:
        case '(':
            floor += 1
        case ')':
            floor -= 1


print(f'Santa has arrived at floor {floor}')
