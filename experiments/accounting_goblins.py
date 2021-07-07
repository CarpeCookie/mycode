#!/usr/bin/env python3

round = 0
#Because of the way my code is setup, it multiplies the correct numbers in every possible permutation to get the right answer
#This means the product of the 3 numbers is calculated and print 6 times, which slows down the code as well
#I decided to just use a "round" to stop the script after it outputs the answer the first time


with open("Expense_Report", "r") as expenses:
    for x in expenses:
#I decided to open the file each time I wanted a new variable, so each are essentially pulling from their own list

        with open("Expense_Report", "r") as cost:
             for y in cost:
#2nd time I'm opening the file 

                 with open("Expense_Report", "r") as price:
                     for z in price:
#3rd time I'm opening the file

                         if round == 0:
#I started an "if else" statement here to increase the "round".  Starting it any later in the script makes the script execute 6 times, regardless of if it prints or not.

                             if int(x)+int(y)+int(z) == 2020:                           
                                 x = int(x)
                                 y = int(y)
                                 z = int(z)
#I made sure each variable was an integer.  This also made the print function look way cleaner.

                                 print(x*y*z)
                                 round = round + 1
                         else:
                             break
#This "if else" statement stops the script after it calculates the sum of the numbers once, making to run quicker.

