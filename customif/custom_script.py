#!/usr/bin/env python3
print("What is your number?")
x = input()  
try:
    x = int(x)
    if x == 5: 
        print(x, "is equal to 5.")
    elif x > 5:
        print(x, "is greater than 5.")
    elif x < 5:
        print(x, "is less than 5.")
except ValueError:
    print(x, "is not an integer.")
