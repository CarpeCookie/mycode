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


def main():
    print("Main Menu: \n1: Equipped Gear\n2: Lore\n3: Match History (Crucible)\n4: Match History (Strikes)\n5: Clan info\n6: Exit Script")
    Main_Menu = input()
    if Main_Menu == "1":
        Equipped_Gear_Menu()
    elif Main_Menu == "6":
        quit()
    else:
        print("Invalid Input. Try Again.")
        main()

#The Main Menu. Its actually an extremely simple function despite being the main function.  It just calls on other functions so I can keep things organized and loop around my script without closing out of it.



def Equipped_Gear_Menu():
    print("Equipped Gear:\n1: Print Gear\n2: Print Stats\n3. How's Your Look?\n4. Go Back\n5: Quit")
    Equipped_Gear = input()
    if Equipped_Gear == "1":
        Print_Gear()
    elif Equipped_Gear == "2":
        Print_Stats()
 #   elif Equipped_Gear == "3":
 #       Check_Fashion()
    elif Equipped_Gear == "4":
        main()
    elif Equipped_Gear == "5":
        quit()
    else:
        print("Invalid Input. Try Again.")
        Equipped_Gear_Menu()

#This is a simple submenu to implement, since I don't need to make any requests to the API at this point.  Again, by compartmentalizing, I make my script easier to manage and easier to navigate.


def Print_Gear():
    print("For which Character?\n1: Warlock\n2: Hunter\n3: Titan")
    Character = input()
    if Character == "1":
        x = requests.get("https://www.bungie.net/Platform/Destiny2/2/Profile/" + membershipId + "/Character/" + warlockid + "/?components=205", headers=HEADERS)
        y = x.json()
        print(y)
        Equipped_Gear_Menu()
    elif Character == "2":
        x = requests.get("https://www.bungie.net/Platform/Destiny2/2/Profile/" + membershipId + "/Character/" + hunterid + "/?components=205", headers=HEADERS)
        y = x.json()
        print(y)
        Equipped_Gear_Menu()
    elif Character == "3":
        x = requests.get("https://www.bungie.net/Platform/Destiny2/2/Profile/" + membershipId + "/Character/" + titanid + "/?components=205", headers=HEADERS)
        y = x.json()
        print(y)
        Equipped_Gear_Menu()
#One of the more complex scripts.  It calls on some of the variables at the start of the script to issue GET Requests to the API.  Then it calls back on the previous function to loop indefinitely.


def Print_Stats():
    print("For which Character?\n1: Warlock\n2: Hunter\n3: Titan")
    Character = input()  
    character_stats = requests.get("https://www.bungie.net/Platform/Destiny2/2/Profile/" + membershipId + "/?components=200", headers=HEADERS)
    character_stats = character_stats.json()
    character_stats_response = character_stats['Response']
    character_stats_characters = character_stats_response['characters']
    character_stats_data = character_stats_characters['data']
    if Character == "1":
        character_stats_id = character_stats_data[warlockid]
        character_stats_stats = character_stats_id['stats']
        print("\n \n")
        print("Warlock:")
        print("Light Level: ",  character_stats_stats['1935470627'])
        print("Intellect: ", character_stats_stats['144602215'])
        print("Strength: ", character_stats_stats['392767087'])
        print("Discipline: ", character_stats_stats['1735777505'])
        print("Recovery: ", character_stats_stats['1943323491'])
        print("Mobility: ", character_stats_stats['2996146975'])
        print("Resilience: ", character_stats_stats['4244567218'])
        print("\n \n")
        Equipped_Gear_Menu()
    elif Character == "2":
        character_stats_id = character_stats_data[hunterid]
        character_stats_stats = character_stats_id['stats']
        print("\n \n")
        print("Hunter:")
        print("Light Level: ",  character_stats_stats['1935470627'])
        print("Intellect: ", character_stats_stats['144602215'])
        print("Strength: ", character_stats_stats['392767087'])
        print("Discipline: ", character_stats_stats['1735777505'])
        print("Recovery: ", character_stats_stats['1943323491'])
        print("Mobility: ", character_stats_stats['2996146975'])
        print("Resilience: ", character_stats_stats['4244567218'])
        print("\n \n")
        Equipped_Gear_Menu()
    elif Character == "3":
        character_stats_id = character_stats_data[titanid]
        character_stats_stats = character_stats_id['stats']
        print("\n \n")
        print("Titan:")
        print("Light Level: ",  character_stats_stats['1935470627'])
        print("Intellect: ", character_stats_stats['144602215'])
        print("Strength: ", character_stats_stats['392767087'])
        print("Discipline: ", character_stats_stats['1735777505'])
        print("Recovery: ", character_stats_stats['1943323491'])
        print("Mobility: ", character_stats_stats['2996146975'])
        print("Resilience: ", character_stats_stats['4244567218'])
        print("\n \n")
        Equipped_Gear_Menu()
    elif Character == "4":
        Equipped_Gear_Menu()
    elif Character == "5":
        quit()
    else:
        print("Invalid Input. Try Again")
        Print_Stats()


#def Check_Fashion():



main()
