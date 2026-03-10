#Rules for nice string
#- String needs to contain a pair of letters that appears at least twice in the
#  string without overlapping.
#- It contains atleast one letter repeating with exactly one letter between it

#Dictionary for listing the different pairs in a string? Value is appearances?
nice_string_count = 0
with open("input.md", "r", encoding='utf-8') as f:
    for line in f:
        lettercount = 0
        pair_dict = {}
        repeated_letter_with_gap = False
        two_pair = False
        line = line.strip("\n")
        for char in line:
            if (lettercount == 0 ):
                lettercount += 1
                continue
            #Key error on check if not registered yet in dict.
            #Should I try-except?
            '''
            if (pair_dict[f'{line[lettercount-1] + char}'] == 1 and \
                char != line[lettercount-1] != line[lettercount - 2]):
                two_pair = True
            else:
                pair_dict[f'{lettercount-1 + char}'] = 1
            '''
            try:
                if (pair_dict[f'{line[lettercount-1] + char}'] == 1):
                    #This exclusively checks for occurrences of three letters
                    #in a row for pair overlaps, which are the only type of
                    #pair overlap possible
                    if (not(char == line[lettercount -1] == \
                        line[lettercount -2] != line[lettercount - 3])):
                        two_pair = True
            except KeyError:
                pair_dict[f'{line[lettercount-1] + char}'] = 1
                pass

            if (lettercount > 1):
                if (char == line[lettercount -2]):
                    repeated_letter_with_gap = True
            lettercount +=1
        if(repeated_letter_with_gap == True and two_pair == True):
            nice_string_count += 1
print(f"There are {nice_string_count} nice strings in the supplied list.")
