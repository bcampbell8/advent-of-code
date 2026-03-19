#Do I need to edit the string, or should i just add extra to the character count each time I encounter a backslash?

import re
import pdb

def mem_counter(string):
    #r = iter(range(len(string.strip('"'))))
    #if(string[0:3] == 'njr'):
        #breakpoint()
    raw_encode_count = 2 # each string has new quotations added, and the previous quotations get an extra backslash to escape for them.
    #breakpoint()
    pos = 0

    while pos < len(string):
    #for i in r:

        if (string[pos] == '\\'):
            #breakpoint()
            #need 4 backslashses to match a single in string backslash if not
            #using raw strings (r'') (which don't parse backslash escapes),
            #because parser for regex needs to escape the backslash
            #e.g regex("\\\\") is interpreted as regex(\\), which is now a
            #regex matching a single backslash. more info:
            #https://stackoverflow.com/questions/4025482/cant-escape-the-backslash-in-a-regular-expression
            raw_encode_count += 1
        elif(string[pos] == '\"'):
            raw_encode_count += 1


        raw_encode_count += 1
        pos+=1

    #print(raw_encode_count)
    return raw_encode_count

with open("input.md", "r", encoding="utf-8") as f:
    raw_character_count = 0
    raw_encode_count = 0
    for line in f:
        #breakpoint()

        line=line.strip("\n")
        raw_character_count += len(line)
        print(line)
        #had to get rid of stripping the quotations because it was messing up strings that had multiple quotations at the end (stripping them all)
        #char_count = 0
        raw_encode_count += mem_counter(line)
        print(mem_counter(line))
        '''
        r = iter(range(len(line)))
        for i in r:
            if (line[i] == '\"'):
                next(r)
            if (line[i] == '\\'):
                #breakpoint()
                #need 4 backslashses to match a single in string backslash if not
                #using raw strings (r'') (which don't parse backslash escapes),
                #because parser for regex needs to escape the backslash
                #e.g regex("\\\\") is interpreted as regex(\\), which is now a
                #regex matching a single backslash. more info:
                #https://stackoverflow.com/questions/4025482/cant-escape-the-backslash-in-a-regular-expression
                if(re.match(r"\\x[a-f, 0-9]{2}",line[i:i+4])):
                    next(r)
                    next(r)
                    next(r)
                else:
                    next(r)
            in_memory_count += 1
        '''

print(raw_character_count)
print(raw_encode_count)
print(raw_encode_count - raw_character_count)
#2310 too high
#2055 too low

print(r"A string of '\\\\on' is counted as " +f"{mem_counter("\\\\on")}")
#breakpoint()
print(r"A string of '\x68' is counted as " +f"{mem_counter("\\x68")}")
