#!/usr/bin/env python3

x = input()
#this assigns a name to the input.  It can be anything, but "x" is a lot quicker to type.

count = 0
#keeps track of how many letters are in the string
for a in x:
    if a == '[a-z]':
        count = count + 1
#counts the number of lowercase letters in the string

for a in x:
    if a == '[A-Z]':
        count = count + 1
#counts the number of uppercase letters in the string

print(count)
