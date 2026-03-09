#This is identical to the 1 star solution except they want to find the number
#for a hash with 6 zeroes instead of 5.

import hashlib

hashsample = "000000"
counter = 0
secret_key = 'bgvyzdsv'

while True:
    altered_key = secret_key + f'{counter}'
    output = hashlib.md5(altered_key.encode()).hexdigest()
    if (output[:6] == hashsample):
        print(f"Secret key {secret_key} with the number {counter} produces a key of {altered_key} with a hash of {output}")
        break
    counter += 1
