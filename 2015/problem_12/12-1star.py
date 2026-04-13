import pdb

total = 0
with open("input.md", "r", encoding='utf-8') as f:
    readout = f.read()
    number = False
    negative = False
    current_number = []
    for char in readout:
        if char.isdigit():
           number = True
           current_number.append(char)
        else:
            if number == True:
                number = False
                current_number = int("".join(current_number))
                if negative == True:
                    total -= current_number
                    negative = False
                else:
                    total += current_number
                current_number = []
            if char == '-':
                negative = True
            else:
                negative = False
print(total)
