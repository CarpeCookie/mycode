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
#This pulls on the API to gather character IDs, which are needed for some specific get requests.  Each Player Profile can have up to 3 characters, who each have a unique ID.  This makes it way simplier to call on the variable instead of handjam the ID or, worse, perform this GET request each time I need a character ID.



print("Welcome to Matt's Test App! Utilizing the the Bungie API, we can gather information on your character from Destiny 2!")
#The welcome line.  I don't want this to keep displaying so this will be outside of any functions.


def Main_Menu():
    print("\nMain Menu: \n1: Equipped Gear\n2: Lore\n3: Match History (Crucible)\n4: Match History (Strikes)\n5: Clan info\n6: Exit Script")
    Main_Menu_Input = input()
    if Main_Menu_Input == "1":
        Equipment_Menu()
    elif Main_Menu_Input == "2":
        Lore_Menu()
    elif Main_Menu_Input == "3":
        Crucible_Menu()
    elif Main_Menu_Input == "4":
        Strike_Menu()
    elif Main_Menu_Input == "5":
        Clan_Menu()
    elif Main_Menu_Input == "6":
        quit()
    else:
        print("\n \nInvalid Input. Try Again.\n \n")
        Main_Menu()

#The Main Menu. Its actually an extremely simple function despite being the main function.  It just calls on other functions so I can keep things organized and loop around my script without closing out of it.






















Main_Menu()
#Call the Main_Menu function to start the script
