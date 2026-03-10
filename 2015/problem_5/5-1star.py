#Nice strings must:
#- Have at least 3 vowel occurrences
#- At least one occurrence of the same letter appearing consecutively
#- Not contain the string 'ab', 'cd', 'pq' or 'xy'
import pdb

nice_string_count = 0
with open("input.md", "r", encoding='utf-8') as f:
    for line in f:
        lettercount = 0
        vowelcount = 0
        three_vowel = False
        consecutive_letter = False
        naughty_string_contain = False
        line = line.strip("\n")
        #breakpoint()
        for char in line:
            if(char == 'a' or char == 'e' or char == 'i' or char == 'o' or \
                char == 'u'):
                vowelcount +=1
            if(lettercount > 0):
                if(line[lettercount-1] == char):
                    consecutive_letter = True
                if(vowelcount == 3):
                    three_vowel = True
                match char:
                    case 'b':
                        if (line[lettercount-1] == 'a'):
                            naughty_string_contain = True
                            break
                    case 'd':
                        if (line[lettercount-1] == 'c'):
                            naughty_string_contain = True
                            break
                    case 'q':
                        if (line[lettercount-1] == 'p'):
                            naughty_string_contain = True
                            break
                    case 'y':
                        if (line[lettercount-1] == 'x'):
                            naughty_string_contain = True
                            break
            lettercount +=1
        if(naughty_string_contain == False and consecutive_letter == True and \
            three_vowel == True):
            nice_string_count += 1
print(f"There are {nice_string_count} nice strings in the supplied list.")
