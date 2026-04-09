This problem posed two main challenges:
- Firstly, getting the regex to work precisely. I thought I'd be able to use 
regex split to split the string up based on the repetition of characters. I was
able to do this but the split functions, to my current understanding, split 
strings on delimiters. This means split wouldn't easily work for my strings 
which weren't inherently split by characters, but a change of character. I 
instead used the `re.findall()` function which finds all matches, and throws
them into a list, along with the last character of the pattern. This ended up 
proving useful later when I needed to reassess how I created each new string.
- The second issue was with the creation of subsequent strings to calculate. 
The last couple strings took forever to calculate and I was unsure why. After 
some googling and reading a suggestion to time the different parts I soon found
the culprit, it was creating a new string that was specifically eating up my 
time. I wasn't sure how I could improve my current solution as the help 
someone else had received recommended using in place string mutation, but in
python strings are immutable. I then read somewhere about using .join(), a 
string method which is capable of concatenating all memebers of a list. I then 
also found that in python's docs that for sequence types (like lists) 
concatenating results in a new object, reaffirming what I'd seen earlier, and 
that 'building up a sequence by repeat concatenation will have a quadratic 
runtime cost in the total sequence length'. This alligned with what I'd 
measured, as from beyond the 40th iteration the following iterations took 
1, 2, 4, 8, 16, 32 ... seconds approximately to complete! So I instead 
manipulated the list I'd created running the `re.findall()` function and then 
ran a join and the total run time of the entire program had shrunk to 12 
seconds. Good enough.
https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
