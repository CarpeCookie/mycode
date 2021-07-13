#!/usr/bin/env python3

import requests
import json

HEADERS = {"X-API-Key":'c6b881de35a143f98cda3d1e5dbf27b4'}


username = input("Username:\n")
membershiptype = input("Input platform type.  1 = Xbox, 2 = Playstation, 3 = Steam, 5 = Stadia\n")

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


def main():
    print("Main Menu: \n1: Equipped Gear\n2: Lore\n3: Crucible (PvP)\n4: Strikes (PvE)\n5: Clan info\n6: Exit Script")
    Main_Menu = input()
    if Main_Menu == "1":
        Equipped_Gear_Menu()
    elif Main_Menu == "3":
        Crucible_Menu()
    elif Main_Menu == "6":
        quit()
    else:
        print("Invalid Input. Try Again.")
        main()

#The Main Menu. Its actually an extremely simple function despite being the main function.  It just calls on other functions so I can keep things organized and loop around my script without closing out of it.



def Crucible_Menu():
    print("Crucible Menu: \n1. Warlock\n2. Hunter\n3. Titan\n4. Main Menu\n5. Quit")    
    Crucible_Menu = input()
    if Crucible_Menu == "1":
        Warlock_Crucible_History()
    elif Crucible_Menu == "2":
        Hunter_Crucible_History()
    elif Crucible_Menu == "3":
        Titan_Crucible_History()
    elif Crucible_Menu == "4":
        main()
    elif Crucible_Menu == "5":
        quit()
    else:
        print("Invalid Input. Try Again.")
        Crucible_Menu()

def Warlock_Crucible_History():    
    print("Crucible Menu: \n1. Match One\n2. Match Two\n3. Match 3\n4. Match 4\n5. Match 5\n6. Main Menu\n7. Quit")
    Crucible_History_Menu = input()
    if Crucible_History_Menu == "1":
        warlock_history = requests.get("https://www.bungie.net/Platform/Destiny2/" + membershiptype + "/Account/" + membershipId + "/Character/" + warlockid + "/Stats/Activities/?count=5&mode=5&page=0", headers=HEADERS)
        warlock_history = warlock_history.json()
        warlock_history_response = warlock_history['Response']
        warlock_history_activities = warlock_history_response['activities']
        warlock_history_match = warlock_history_activities['0']
        warlock_history_stats = warlock_history_match['values']
        print(warlock_history_stats)
        print("\n \n")
        

    
    
    
    
    
    
    
main()
