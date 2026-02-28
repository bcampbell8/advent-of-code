f = open("input.txt", "r", encoding="utf-8")
instructions = f.read()
floor = 0
base_check = False
position = 0
#breakpoint()
print(len(instructions))
for x in instructions:
    position += 1
    match x:
        case '(':
            floor += 1
        case ')':
            floor -= 1
    if (floor < 0 and base_check is False):
        base_check = True
        print(f"Santa goes to the basement at position {position}")


print(f'Santa has arrived at floor {floor}')
