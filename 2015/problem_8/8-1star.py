#Need to count the number of characters in a string, and also their in memory
#values e.g what escape characters are evaluated to

import re
import pdb

#!!CASE TO INVESTIGATE: three backslashes (where two are an escaped backslash and the third is the beginning of a hex character)

def mem_counter(string):
    #r = iter(range(len(string.strip('"'))))
    #if(string[0:3] == 'njr'):
        #breakpoint()
    in_memory_count = 0
    pos = 0
    while pos < len(string):
    #for i in r:
        #breakpoint()
        if (string[pos] == '\\'):
            #breakpoint()
            #need 4 backslashses to match a single in string backslash if not
            #using raw strings (r'') (which don't parse backslash escapes),
            #because parser for regex needs to escape the backslash
            #e.g regex("\\\\") is interpreted as regex(\\), which is now a
            #regex matching a single backslash. more info:
            #https://stackoverflow.com/questions/4025482/cant-escape-the-backslash-in-a-regular-expression

            if(re.match(r"\\x[a-f, 0-9]{2}",string[pos:pos+4])):
                pos+=3


            else:
                pos+=1

        in_memory_count += 1
        pos+=1

    #print(in_memory_count)
    return in_memory_count

with open("input.md", "r", encoding="utf-8") as f:
    raw_character_count = 0
    in_memory_count = 0
    for line in f:
        #breakpoint()

        line=line.strip("\n")
        raw_character_count += len(line)
        line = line.strip('"')
        print(line)

        #char_count = 0
        in_memory_count += mem_counter(line)
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
print(in_memory_count)
print(raw_character_count - in_memory_count)


print(r"A string of '\\\\on' is counted as " +f"{mem_counter("\\\\on")}")
#breakpoint()
print(r"A string of '\x68' is counted as " +f"{mem_counter("\\x68")}")
