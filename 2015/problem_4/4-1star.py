#So the goal of this seems to be to find the smallest number that produces a
#hash with 5 leading zeros, using my input. I.e I need to find a number that
#follows my puzzle input (bgvyzdsv) that hashes to a string with atleast 5
#leading zeroes.

import hashlib

hashsample = "00000"
counter = 0
secret_key = 'bgvyzdsv'
#The method below was giving me the wrong output. Creating a new hash with
#new() creates a hash from all the data supplied to it thus far. So it wasn't
#hashing a single key at a time but a combination of all previously fed.

f = open('strings.md', "w", encoding="utf-8")
while True:
    altered_key = secret_key + f'{counter}'
    output = hashlib.md5(altered_key.encode()).hexdigest()
    if (output[:5] == hashsample):
        print(f"Secret key {secret_key} with the number {counter} produces a key of {altered_key} with a hash of {output}")
        f.write(f"=========================================================================================\n")
        f.write(f"Secret key {secret_key} with the number {counter} produces a key of {altered_key} with a hash of {output}\n")
        f.write(f"=========================================================================================")
        break
    f.write(f"Secret key {secret_key} with the number {counter} produces a key of {altered_key} with a hash of {output}\n")
    counter += 1
f.close()

