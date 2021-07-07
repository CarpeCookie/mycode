#!/usr/bin/env python3

kitchen = {"pan":"tool","spoon":"tool","yo-yo":"toy","banana":"food","jump rope":"toy","stove":"appliance"}

for key, value in kitchen.items():
    if value == 'toy':
        print("success")
