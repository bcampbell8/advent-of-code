#So the goal of this seems to be to find the smallest number that produces a
#hash with 5 leading zeros, using my input. I.e I need to find a number that
#follows my puzzle input (bgvyzdsv) that hashes to a string with atleast 5
#leading zeroes.

#Takeaways
#To create a hash in python we can use the hashlib which comes as a default.
#First you create a key for the hashing algorithm to use, then encode it as a
#byte string (which can be done using 'b' before a string similar to f-strings)
#then hash it using the hashing algorithm of your choice. This returns a hash
#object which you then use hexdigest() to get the hexadecimal of the hash.

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

