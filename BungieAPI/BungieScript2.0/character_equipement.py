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


def Main_Menu():
    print("Main Menu: \n1: Equipped Gear\n2: Lore\n3: Match History (Crucible)\n4: Match History (Strikes)\n5: Clan info\n6: Exit Script")
    Main_Menu = input()
    if Main_Menu == "1":
        Equipment_Menu()
    elif Main_Menu == "6":
        quit()
    else:
        print("Invalid Input. Try Again.")
        Main_Menu()


def Equipment_Menu():
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
        print("\n \nInvalid Input. Try Again.\n \n")
        Equipment_Menu()
   
    
def Print_Gear():    
    print("For which Character?\n1: Warlock\n2: Hunter\n3: Titan\n4: Equipment Menu\n5: Main Menu\n6: Quit")
    Character = input()
    if Character == "1":
        gear = requests.get("https://www.bungie.net/Platform/Destiny2/2/Profile/" + membershipId + "/Character/" + warlockid + "/?components=205", headers=HEADERS)
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
    print("For which Character?\n1: Warlock\n2: Hunter\n3: Titan\n4: Equipment Menu\n5: Main Menu\n6: Quit")
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
        Print_Stats()
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
