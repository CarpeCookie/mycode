#!/usr/bin/env python3

import requests
import json

HEADERS = {"X-API-Key":'c6b881de35a143f98cda3d1e5dbf27b4'}
searchdestinyprofile = requests.get("https://www.bungie.net/Platform/Destiny2/SearchDestinyPlayer/2/CarpeCookie", headers=HEADERS)
# we do this request to pull user profile information.  This is the first request and doesn't require backend information, just the username and console.

destinyprofile = searchdestinyprofile.json()    

#the dictiontary its placed into
membershiptype = "2"

destinyprofile_response = destinyprofile['Response']
destinyprofile_data = destinyprofile_response[0]
membershipId = destinyprofile_data['membershipId']
#breaking down the dictionary since I don't know how to search the subsections with a string.  I'll likely be using the membershipId often, so I just assigned it its own name.  I won't have to keep using a command to pull it from the list.  Also, the name of the value will be the same as the API I'm pulling from, making it easier to understand.

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

getclan = requests.get("https://www.bungie.net/Platform/GroupV2/Name/FILTHY BOYZ/1/", headers=HEADERS)
getclan = getclan.json()
clanid = getclan['Response']['detail']['groupId']


print("\nWelcome to Matt's Test App! Utilizing the the Bungie API, we can gather information on your character from Destiny 2!")
#The welcome line.  I don't want this to keep displaying so this will be outside of any functions.


def Main_Menu():
    print("\nMain Menu: \n1: Equipped Gear\n2: Match History (Crucible)\n3: Match History (Strikes)\n4: Clan info\n5: Exit Script")
    Main_Menu_Input = input()
    if Main_Menu_Input == "1":
        Equipment_Menu()
    elif Main_Menu_Input == "2":
        Crucible_Menu()
    elif Main_Menu_Input == "3":
        Strike_Menu()
    elif Main_Menu_Input == "4":
        Clan_Menu()
    elif Main_Menu_Input == "5":
        quit()
    else:
        print("\n \nInvalid Input. Try Again.\n \n")
        Main_Menu()

#The Main Menu. Its actually an extremely simple function despite being the main function.  It just calls on other functions so I can keep things organized and loop around my script without closing out of it.

def Equipment_Menu():
    print("\nEquipped Gear:\n1: Print Gear\n2: Print Stats\n3: How's Your Look?\n4: Main Menu\n5: Quit")
    Equipped_Gear = input()
    if Equipped_Gear == "1":
        Print_Gear()
    elif Equipped_Gear == "2":
        Print_Stats()
 #   elif Equipped_Gear == "3":
 #       Check_Fashion()
    elif Equipped_Gear == "4":
        Main_Menu()
    elif Equipped_Gear == "5":
        quit()
    else:
        print("\n \nInvalid Input. Try Again.\n \n")
        Equipment_Menu()
#The Equipment submenu.  Same logic as the Main_Menu.  Simplify it by calling other functions.
    
def Print_Gear():    
    print("\nFor which Character?\n1: Warlock\n2: Hunter\n3: Titan\n4: Equipment Menu\n5: Main Menu\n6: Quit")
    Character = input()
    if Character == "1":
        gear = requests.get("https://www.bungie.net/Platform/Destiny2/2/Profile/" + membershipId + "/Character/" + warlockid + "/?components=205", headers=HEADERS)
        gear = gear.json()
        gear = gear['Response']['equipment']['data']['items']
#This performs the GET Request and then breaks it down to the lowest level I can before I need break down individual items.

        helmet = gear[3]['itemHash']
        helmet_info = requests.get("https://www.bungie.net/Platform/Destiny2/Manifest/DestinyInventoryItemDefinition/" + str(helmet), headers=HEADERS)
        helmet_info = helmet_info.json()
        helmet_info = helmet_info['Response']['displayProperties']['name']
#This starts off by pulling the "Item Hash" which is specific for each item.  The second GET Request uses that hash to pull the Item's information.  I then break down that GET request until I get the item's name.  Unfortunately, an item's name isn't in the first GET Request, so I need to use this ugly code just to pull a name.  I repeat it for each armor piece.

        gloves = gear[4]['itemHash']
        gloves_info = requests.get("https://www.bungie.net/Platform/Destiny2/Manifest/DestinyInventoryItemDefinition/" + str(gloves), headers=HEADERS)
        gloves_info = gloves_info.json()
        gloves_info = gloves_info['Response']['displayProperties']['name']
        chest = gear[5]['itemHash']
        chest_info = requests.get("https://www.bungie.net/Platform/Destiny2/Manifest/DestinyInventoryItemDefinition/" + str(chest), headers=HEADERS)
        chest_info = chest_info.json()
        chest_info = chest_info['Response']['displayProperties']['name']
        boots = gear[6]['itemHash']
        boots_info = requests.get("https://www.bungie.net/Platform/Destiny2/Manifest/DestinyInventoryItemDefinition/" + str(boots), headers=HEADERS)
        boots_info = boots_info.json()
        boots_info = boots_info['Response']['displayProperties']['name']
        class_item = gear[7]['itemHash']
        class_item_info = requests.get("https://www.bungie.net/Platform/Destiny2/Manifest/DestinyInventoryItemDefinition/" + str(class_item), headers=HEADERS)
        class_item_info = class_item_info.json()
        class_item_info = class_item_info['Response']['displayProperties']['name']
       
        print("\n \nHelmet: ", helmet_info)
        print("Gloves: ", gloves_info)
        print("Chest: ", chest_info)
        print("Boots: ", boots_info)
        print("Class Item: ", class_item_info)
        print("\n \n")
        Print_Gear()
#Printing the Item names.  Calls on the variables made in the previous part of the script.

    elif Character == "2":
        gear = requests.get("https://www.bungie.net/Platform/Destiny2/2/Profile/" + membershipId + "/Character/" + hunterid + "/?components=205", headers=HEADERS)
        gear = gear.json()
        gear = gear['Response']['equipment']['data']['items']
        helmet = gear[3]['itemHash']
        helmet_info = requests.get("https://www.bungie.net/Platform/Destiny2/Manifest/DestinyInventoryItemDefinition/" + str(helmet), headers=HEADERS)
        helmet_info = helmet_info.json()
        helmet_info = helmet_info['Response']['displayProperties']['name']
        gloves = gear[4]['itemHash']
        gloves_info = requests.get("https://www.bungie.net/Platform/Destiny2/Manifest/DestinyInventoryItemDefinition/" + str(gloves), headers=HEADERS)
        gloves_info = gloves_info.json()
        gloves_info = gloves_info['Response']['displayProperties']['name']
        chest = gear[5]['itemHash']
        chest_info = requests.get("https://www.bungie.net/Platform/Destiny2/Manifest/DestinyInventoryItemDefinition/" + str(chest), headers=HEADERS)
        chest_info = chest_info.json()
        chest_info = chest_info['Response']['displayProperties']['name']
        boots = gear[6]['itemHash']
        boots_info = requests.get("https://www.bungie.net/Platform/Destiny2/Manifest/DestinyInventoryItemDefinition/" + str(boots), headers=HEADERS)
        boots_info = boots_info.json()
        boots_info = boots_info['Response']['displayProperties']['name']
        class_item = gear[7]['itemHash']
        class_item_info = requests.get("https://www.bungie.net/Platform/Destiny2/Manifest/DestinyInventoryItemDefinition/" + str(class_item), headers=HEADERS)
        class_item_info = class_item_info.json()
        class_item_info = class_item_info['Response']['displayProperties']['name']
        print("\n \nHelmet: ", helmet_info)
        print("Gloves: ", gloves_info)
        print("Chest: ", chest_info)
        print("Boots: ", boots_info)
        print("Class Item: ", class_item_info)
        print("\n \n")
        Print_Gear()

    elif Character == "3":
        gear = requests.get("https://www.bungie.net/Platform/Destiny2/2/Profile/" + membershipId + "/Character/" + titanid + "/?components=205", headers=HEADERS)
        gear = gear.json()
        gear = gear['Response']['equipment']['data']['items']
        helmet = gear[3]['itemHash']
        helmet_info = requests.get("https://www.bungie.net/Platform/Destiny2/Manifest/DestinyInventoryItemDefinition/" + str(helmet), headers=HEADERS)
        helmet_info = helmet_info.json()
        helmet_info = helmet_info['Response']['displayProperties']['name']
        gloves = gear[4]['itemHash']
        gloves_info = requests.get("https://www.bungie.net/Platform/Destiny2/Manifest/DestinyInventoryItemDefinition/" + str(gloves), headers=HEADERS)
        gloves_info = gloves_info.json()
        gloves_info = gloves_info['Response']['displayProperties']['name']
        chest = gear[5]['itemHash']
        chest_info = requests.get("https://www.bungie.net/Platform/Destiny2/Manifest/DestinyInventoryItemDefinition/" + str(chest), headers=HEADERS)
        chest_info = chest_info.json()
        chest_info = chest_info['Response']['displayProperties']['name']
        boots = gear[6]['itemHash']
        boots_info = requests.get("https://www.bungie.net/Platform/Destiny2/Manifest/DestinyInventoryItemDefinition/" + str(boots), headers=HEADERS)
        boots_info = boots_info.json()
        boots_info = boots_info['Response']['displayProperties']['name']
        class_item = gear[7]['itemHash']
        class_item_info = requests.get("https://www.bungie.net/Platform/Destiny2/Manifest/DestinyInventoryItemDefinition/" + str(class_item), headers=HEADERS)
        class_item_info = class_item_info.json()
        class_item_info = class_item_info['Response']['displayProperties']['name']
        print("\n \nHelmet: ", helmet_info)
        print("Gloves: ", gloves_info)
        print("Chest: ", chest_info)
        print("Boots: ", boots_info)
        print("Class Item: ", class_item_info)
        print("\n \n")
        Print_Gear()

    elif Character == "4":
        Equipment_Menu()

    elif Character == "5":
        Main_Menu()

    elif Character == "6":
        quit()

    else:
        print("\n \nInvalid Input. Try Again.\n \n")
        Print_Gear()

def Print_Stats():
    print("\nFor which Character?\n1: Warlock\n2: Hunter\n3: Titan\n4: Equipment Menu\n5: Main Menu\n6: Quit")
    Character = input()
    character_stats = requests.get("https://www.bungie.net/Platform/Destiny2/2/Profile/" + membershipId + "/?components=200", headers=HEADERS)
    character_stats = character_stats.json()
    character_stats_response = character_stats['Response']
    character_stats_characters = character_stats_response['characters']
    character_stats_data = character_stats_characters['data']
#Pulls Information that will responsd with all character stats.  I break it down until it would specify a character.
    
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
        Print_Stats()
#breaks the code down further depending on input to acquire the specified character's stats.

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
        Print_Stats()
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
        Print_Stats()
    elif Character == "4":
        Equipment_Menu()
    elif Character == "5":
        Main_Menu()
    elif Character == "6":
        quit()
    else:
        print("\n \nInvalid Input. Try Again\n \n")
        Print_Stats()

Main_Menu()
