#password = 'hepxcrrq'

'''
How do I check each rule?
1. Passwords must contain a 'straight' of three 'increasing' letters
2. Passwords cannot contain i, o or l
3. Passwords must contain two different, non-overlapping pairs of letters
4. Passwords can only be 8 characters in length
'''

import re
import pdb


def rule_check(password):
    if(len(password) != 8):
        return False
    #is it better to just put this all in one regex ruling?
    if(re.match('[iol]', password)):
        return False
    if(len(re.findall(r'(\D)\1', password)) != 2):
        return False
    count = 0
    for i in range(len(password)):
        if i == 0:
            continue
        if ord(password[i-1]) == ord(password[i]) - 1:
            count += 1
        else:
            count = 0
        if count == 2:
            return True
    return False

def iterate_password(password):
    #breakpoint()
    current_password = list(password)
    if current_password[7] == 'z':
        place = 7
        while current_password[place] == 'z':
            current_password[place] = 'a'
            place -= 1
        current_password[place] = chr(ord(current_password[place])+1)
    else:
        current_password[7] = chr(ord(current_password[7])+1)
    password = ''.join(current_password)
    return password

def main():
    password = 'hepxcrrq'
    new_password = password
    while rule_check(new_password) == False:
        new_password = iterate_password(new_password)
    second_password = iterate_password(new_password)
    while rule_check(second_password) == False:
        second_password = iterate_password(second_password)
    print(f"Santa's first password is: {new_password}, and his second password is: {second_password}")

main()







