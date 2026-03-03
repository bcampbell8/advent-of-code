present_tally_s1 = {}
present_tally_s2 = {}
with open("input.md", "r", encoding="utf-8") as f:
    directions = f.read()
    x = 0
    y = 0
    xp = 0
    yp = 0
    counter = 0
    present_tally_s1[f'{[x,y]}'] = 1
    present_tally_s1[f'{[xp,yp]}'] = 1
    for loc in directions:
        counter += 1
        #I don't really like copy-pasting the same code twice.
        #I wonder if there's a cleaner/more concise way to do this.
        if counter %2 == 1:
            match loc:
                case '>':
                    x +=1
                case '<':
                    x -= 1
                case '^':
                    y += 1
                case 'v':
                    y -= 1
            if f'{[x,y]}' not in present_tally_s1:
                present_tally_s1[f'{[x,y]}'] = 1
            else:
                present_tally_s1[f'{[x,y]}'] += 1

            #Wanted to try doing this with ternary operator. Python uses an
            #inline if else instead with different ordering of arguments
            #compared to other languages.
            #https://stackoverflow.com/questions/394809/does-python-have-a-ternary-conditional-operator
            #This was discarded though as I need to do more conditional
            #logic later anyway, so it's probably better to just do the
            #conditional of whether it's santa 1 or 2 at the start.
            """
            case '>':
                x +=1 if counter % 2 == 1 else xp += 1
            case '<':
                x -= 1 if counter % 2 == 1 else xp -= 1
            case '^':
                y += 1 if counter % 2 == 1 else yp += 1
            case 'v':
                y -= 1 if counter % 2 == 1 else yp -= 1
            """
        else:
            match loc:
                case '>':
                    xp +=1
                case '<':
                    xp -= 1
                case '^':
                    yp += 1
                case 'v':
                    yp -= 1
            if f'{[xp,yp]}' not in present_tally_s2:
                present_tally_s2[f'{[xp,yp]}'] = 1
            else:
                present_tally_s2[f'{[xp,yp]}'] += 1

#Creates a dictionary merged from the two inputs into a new dictionary.
#The final dictionary has all unique keys, and for the values I think
#it defaults to those given by the second argument.
#https://stackoverflow.com/questions/38987/how-do-i-merge-two-dictionaries-in-a-single-expression-in-python
total_tally = present_tally_s1 | present_tally_s2
print(len(list(total_tally)))

