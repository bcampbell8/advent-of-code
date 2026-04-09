#Input: 1113122113

'''
Pseudocode
1. Create empty string
2. Parse input string, Break input string down to groups of repeating numbers.
3. Number of times a digit is repeated plus the digit itself is concatenated to newly created string.
4. Repeat for each group of numbers.
5. Repeat entire process on newly generated string.

'''
import re

seed = '1113122113'
for i in range(40):
    new_sequence = ""
    groups = re.findall(r'((.)\2*)', seed)
    parts = []
    for x in groups:
        parts.append(x[0])
    for x in parts:
        new_sequence += str(len(x)) + x[0]
    seed = new_sequence
print(f"Final length: {len(seed)}")
