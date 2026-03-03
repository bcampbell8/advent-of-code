#The big problem here comes from how to represent the information given into an appropriate data structure
#I think the best way to handle this is a dictionary, with a tuple key (x,y co-ord) and then a value of how many presents it gets
present_tally = {}
with open("input.md", "r", encoding="utf-8") as f:
    directions = f.read()
    x = 0
    y = 0
    present_tally[f'{[x,y]}'] = 1
    for loc in directions:
        match loc:
            case '>':
                x += 1
            case '<':
                x -= 1
            case '^':
                y += 1
            case 'v':
                y -= 1
        #Though not strictly necessary, I wanted to count the distinct number of presents each house got because why not?
        if f'{[x,y]}' not in present_tally:
            present_tally[f'{[x,y]}'] = 1
        else:
            present_tally[f'{[x,y]}'] += 1

print(present_tally)
print(len(list(present_tally)))
