#!/usr/bin/env python3

import requests
import json

HEADERS = {"X-API-Key":'c6b881de35a143f98cda3d1e5dbf27b4'}
searchdestinyprofile = requests.get("https://www.bungie.net/Platform/Destiny2/SearchDestinyPlayer/2/CarpeCookie", headers=HEADERS)
# we do this request to pull user profile information.  This is the first request and doesn't require backend information, just the username and console.

destinyprofile = searchdestinyprofile.json()    
#the dictiontary its placed into

destinyprofile_response = destinyprofile['Response']
destinyprofile_data = destinyprofile_response[0]
membershipId = destinyprofile_data['membershipId']
#breaking down the dictionary since I don't know how to search the subsections with a string.  I'll likely be using the membershipId often, so I just assigned it its own name.  I won't have to keep using a command to pull it from the list.  Also, the name of the value will be the same as the API I'm pulling from, making it easier to understand.
print(membershipId)

getprofile = requests.get("https://www.bungie.net/Platform/Destiny2/2/Profile/4611686018465168592/?components=200", headers=HEADERS)
getprofile = getprofile.json()
getprofile_response = getprofile['Response']
getprofile_characters = getprofile_response['characters']
getprofile_data = getprofile_characters['data']
getprofile_data_keys = list(getprofile_data.keys())
warlockid = getprofile_data_keys[0]
hunterid = getprofile_data_keys[1]
titanid = getprofile_data_keys[2]


print("Welcome to Matt's Test App! Utilizing the the Bungie API, we can gather information on your character from Destiny 2!")
print("Main Menu: \n1: Equipped Gear\n2: Lore\n3: Match History (Crucible)\n4: Match History (Strikes)\n5: Clan info\n6: Exit Script")
Main_Menu = input()
if Main_Menu == "1":
    print("Equipped Gear:\n1: Print Gear\n2: Print Stats\n3. How's Your Look?\n4. Go Back\n5: Quit")
    Equipped_Gear = input()
    if Equipped_Gear == "1":
        print("For which Character?\n1: Warlock\n2: Hunter\n3: Titan")
        Character = input()
        if Character == "1":
            x = requests.get("https://www.bungie.net/Platform/Destiny2/2/Profile/" + membershipId + "/Character/" + warlockid + "/?components=205", headers=HEADERS)
            y = x.json()
            print(y)
        elif Character == "2":
            x = requests.get("https://www.bungie.net/Platform/Destiny2/2/Profile/" + membershipId + "/Character/" + hunterid + "/?components=205", headers=HEADERS)
            y = x.json()
            print(y)
        elif Character == "3":
            x = requests.get("https://www.bungie.net/Platform/Destiny2/2/Profile/" + membershipId + "/Character/" + titanid + "/?components=205", headers=HEADERS)
            y = x.json()
            print(y)


