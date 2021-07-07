#!/usr/bin/env python3

round = 0
if round == 0:
    with open("Expense_Report", "r") as expenses:
        for x in expenses:
            with open("Expense_Report", "r") as cost:
                for y in cost:
                    with open("Expense_Report", "r") as price:
                        for z in price:
                            if round == 0:
                                if int(x)+int(y)+int(z) == 2020:                           
                                    x = int(x)
                                    y = int(y)
                                    z = int(z)
                                    print(x*y*z)
                                    round = round + 1
                            else:
                                break
