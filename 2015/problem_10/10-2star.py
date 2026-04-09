import re
import time
import pdb

true_start = time.time()
seed = '1113122113'

for i in range(50):
    start_scan = time.time()
    new_sequence = ""
    #breakpoint()
    groups = re.findall(r'((.)\2*)', seed)
    parts = []
    finish_scan = time.time()
    for x in groups:
        parts.append(str(len(x[0])))
        parts.append(x[1])
    finish_groups = time.time()
    new_sequence = new_sequence.join(parts)
    #print(new_sequence)
    end = time.time()
    seed = new_sequence
    #So sequence construction is the major limiting factor.
    #How would i construct it more efficiently?
    #Figure out elements? concatenate in one line?
    #print(f"new sequence hit: {i}, scan time: {finish_scan - start_scan}s, part-list construction: {finish_groups - finish_scan}s, total time elapsed: {end - start_scan}s ")

#print(re.findall(r'((.)\2*)', seed))

print(f"Final length: {len(seed)}")
true_end = time.time()
print(f"Final run time: {true_end - true_start}")
