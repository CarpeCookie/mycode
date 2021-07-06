#!/usr/bin/env python3

import urllib.request
import re
#importing the necessary libraries

print("Where should we search?")
#telling the user what to enter

url = input()
#the actual line to accept user input

print("Great! So we'll try to open this url " + str(url) + " to search for the phrase:")
#telling the user what it will do with the input

searchFor = input()
#grabbing input with the search function

searchMe = urllib.request.urlopen(url).read().decode("utf-8")
#telling search where to look

if re.search(searchFor, searchMe):
    print("Found a match!")
#what to say on a successful search

else:
    print("No match!")
#what to say on a failed search
