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

getclan = requests.get("https://www.bungie.net/Platform/GroupV2/Name/FILTHY BOYZ/1/", headers=HEADERS)
getclan = getclan.json()
clanid = getclan['Response']['detail']['groupId']


print("Welcome to Matt's Test App! Utilizing the the Bungie API, we can gather information on your character from Destiny 2!")
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
    print("\nEquipped Gear:\n1: Print Gear\n2: Print Stats\n3. How's Your Look?\n4. Go Back\n5: Quit")
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





### LORE MENU ###
### LORE MENU ###
### LORE MENU ###


def Crucible_Menu():
    print("\nCrucible Menu: \n1. Warlock\n2. Hunter\n3. Titan\n4. Main Menu\n5. Quit")    
    Crucible_Menu_Input = input()
    if Crucible_Menu_Input == "1":
        Warlock_Crucible_History()
    elif Crucible_Menu_Input == "2":
        Hunter_Crucible_History()
    elif Crucible_Menu_Input == "3":
        Titan_Crucible_History()
    elif Crucible_Menu_Input == "4":
        main()
    elif Crucible_Menu_Input == "5":
        quit()
    else:
        print("\nInvalid Input. Try Again.\n")
        Crucible_Menu()
#Simple Menu calling on functions to 

def Warlock_Crucible_History():    
    print("\nWarlock Crucible Menu: \n1. Match One\n2. Match Two\n3. Match Three\n4. Match Four\n5. Match Five\n6. Crucible Menu\n7. Main Menu\n8. Quit")
    Crucible_History_Menu = input()
    if Crucible_History_Menu == "1":
        history = requests.get("https://www.bungie.net/Platform/Destiny2/" + membershiptype + "/Account/" + membershipId + "/Character/" + warlockid + "/Stats/Activities/?count=5&mode=5&page=0", headers=HEADERS)
        history = history.json()
        history_response = history['Response']
        history_activities = history_response['activities']
        match = history_activities[0]
        match_stats = match['values']
        assists = match_stats['assists']
        assists = assists['basic']
        assists = assists['value']
        kills = match_stats['kills']
        kills = kills['basic']
        kills = kills['value']
        deaths = match_stats['deaths']
        deaths = deaths['basic']
        deaths = deaths['value']
        KDA =  match_stats['killsDeathsAssists']
        KDA = KDA['basic']
        KDA = KDA['value']
        score = match_stats['score']
        score = score['basic']
        score = score['value']
#Honestly, this code here is trash.  I realized how I could use only a third of the lines here after I finished.  I really want to come back and fix this if I have the time.  It does get the job done though.

        print("\n \nScore: ", score)
        print("Kills: ", kills)
        print("Deaths: ", deaths)
        print("Assists: ", assists)
        print("KDA: :", KDA)
        print("\n \n")
        Warlock_Crucible_History()
        
    elif Crucible_History_Menu == "2":
        history = requests.get("https://www.bungie.net/Platform/Destiny2/" + membershiptype + "/Account/" + membershipId + "/Character/" + warlockid + "/Stats/Activities/?count=5&mode=5&page=0", headers=HEADERS)
        history = history.json()
        history_response = history['Response']
        history_activities = history_response['activities']
        match = history_activities[1]
        match_stats = match['values']
        assists = match_stats['assists']
        assists = assists['basic']
        assists = assists['value']
        kills = match_stats['kills']
        kills = kills['basic']
        kills = kills['value']
        deaths = match_stats['deaths']
        deaths = deaths['basic']
        deaths = deaths['value']
        KDA =  match_stats['killsDeathsAssists']
        KDA = KDA['basic']
        KDA = KDA['value']
        score = match_stats['score']
        score = score['basic']
        score = score['value']
        print("\n \nScore: ", score)
        print("Kills: ", kills)
        print("Deaths: ", deaths)
        print("Assists: ", assists)
        print("KDA: :", KDA)
        print("\n \n")
        Warlock_Crucible_History()
        
    elif Crucible_History_Menu == "3":
        history = requests.get("https://www.bungie.net/Platform/Destiny2/" + membershiptype + "/Account/" + membershipId + "/Character/" + warlockid + "/Stats/Activities/?count=5&mode=5&page=0", headers=HEADERS)
        history = history.json()
        history_response = history['Response']
        history_activities = history_response['activities']
        match = history_activities[2]
        match_stats = match['values']
        assists = match_stats['assists']
        assists = assists['basic']
        assists = assists['value']
        kills = match_stats['kills']
        kills = kills['basic']
        kills = kills['value']
        deaths = match_stats['deaths']
        deaths = deaths['basic']
        deaths = deaths['value']
        KDA =  match_stats['killsDeathsAssists']
        KDA = KDA['basic']
        KDA = KDA['value']
        score = match_stats['score']
        score = score['basic']
        score = score['value']
        print("\n \nScore: ", score)
        print("Kills: ", kills)
        print("Deaths: ", deaths)
        print("Assists: ", assists)
        print("KDA: :", KDA)
        print("\n \n")
        Warlock_Crucible_History()

    elif Crucible_History_Menu == "4":
        history = requests.get("https://www.bungie.net/Platform/Destiny2/" + membershiptype + "/Account/" + membershipId + "/Character/" + warlockid + "/Stats/Activities/?count=5&mode=5&page=0", headers=HEADERS)
        history = history.json()
        history_response = history['Response']
        history_activities = history_response['activities']
        match = history_activities[3]
        match_stats = match['values']
        assists = match_stats['assists']
        assists = assists['basic']
        assists = assists['value']
        kills = match_stats['kills']
        kills = kills['basic']
        kills = kills['value']
        deaths = match_stats['deaths']
        deaths = deaths['basic']
        deaths = deaths['value']
        KDA =  match_stats['killsDeathsAssists']
        KDA = KDA['basic']
        KDA = KDA['value']
        score = match_stats['score']
        score = score['basic']
        score = score['value']
        print("\n \nScore: ", score)
        print("Kills: ", kills)
        print("Deaths: ", deaths)
        print("Assists: ", assists)
        print("KDA: :", KDA)
        print("\n \n")
        Warlock_Crucible_History() 

    elif Crucible_History_Menu == "5":
        history = requests.get("https://www.bungie.net/Platform/Destiny2/" + membershiptype + "/Account/" + membershipId + "/Character/" + warlockid + "/Stats/Activities/?count=5&mode=5&page=0", headers=HEADERS)
        history = history.json()
        history_response = history['Response']
        history_activities = history_response['activities']
        match = history_activities[4]
        match_stats = match['values']
        assists = match_stats['assists']
        assists = assists['basic']
        assists = assists['value']
        kills = match_stats['kills']
        kills = kills['basic']
        kills = kills['value']
        deaths = match_stats['deaths']
        deaths = deaths['basic']
        deaths = deaths['value']
        KDA =  match_stats['killsDeathsAssists']
        KDA = KDA['basic']
        KDA = KDA['value']
        score = match_stats['score']
        score = score['basic']
        score = score['value']
        print("\n \nScore: ", score)
        print("Kills: ", kills)
        print("Deaths: ", deaths)
        print("Assists: ", assists)
        print("KDA: :", KDA)
        print("\n \n")
        Warlock_Crucible_History()

    elif Crucible_History_Menu == "6":    
        Crucible_Menu()

    elif Crucible_History_Menu == "7":
        Main_Menu()

    elif Crucible_History_Menu == "8":
        quit()

    else:
        print("\nInvalid Input. Try Again.\n")
        Warlock_Crucible_History()

def Hunter_Crucible_History():    
    print("\nHunter Crucible Menu: \n1. Match One\n2. Match Two\n3. Match Three\n4. Match Four\n5. Match Five\n6. Crucible Menu\n7. Main Menu\n8. Quit")
    Crucible_History_Menu = input()
    if Crucible_History_Menu == "1":
        history = requests.get("https://www.bungie.net/Platform/Destiny2/" + membershiptype + "/Account/" + membershipId + "/Character/" + hunterid + "/Stats/Activities/?count=5&mode=5&page=0", headers=HEADERS)
        history = history.json()
        history_response = history['Response']
        history_activities = history_response['activities']
        match = history_activities[0]
        match_stats = match['values']
        assists = match_stats['assists']
        assists = assists['basic']
        assists = assists['value']
        kills = match_stats['kills']
        kills = kills['basic']
        kills = kills['value']
        deaths = match_stats['deaths']
        deaths = deaths['basic']
        deaths = deaths['value']
        KDA =  match_stats['killsDeathsAssists']
        KDA = KDA['basic']
        KDA = KDA['value']
        score = match_stats['score']
        score = score['basic']
        score = score['value']
        print("\n \nScore: ", score)
        print("Kills: ", kills)
        print("Deaths: ", deaths)
        print("Assists: ", assists)
        print("KDA: :", KDA)
        print("\n \n")
        Hunter_Crucible_History()
        
    elif Crucible_History_Menu == "2":
        history = requests.get("https://www.bungie.net/Platform/Destiny2/" + membershiptype + "/Account/" + membershipId + "/Character/" + hunterid + "/Stats/Activities/?count=5&mode=5&page=0", headers=HEADERS)
        history = history.json()
        history_response = history['Response']
        history_activities = history_response['activities']
        match = history_activities[1]
        match_stats = match['values']
        assists = match_stats['assists']
        assists = assists['basic']
        assists = assists['value']
        kills = match_stats['kills']
        kills = kills['basic']
        kills = kills['value']
        deaths = match_stats['deaths']
        deaths = deaths['basic']
        deaths = deaths['value']
        KDA =  match_stats['killsDeathsAssists']
        KDA = KDA['basic']
        KDA = KDA['value']
        score = match_stats['score']
        score = score['basic']
        score = score['value']
        print("\n \nScore: ", score)
        print("Kills: ", kills)
        print("Deaths: ", deaths)
        print("Assists: ", assists)
        print("KDA: :", KDA)
        print("\n \n")
        Hunter_Crucible_History()
        
    elif Crucible_History_Menu == "3":
        history = requests.get("https://www.bungie.net/Platform/Destiny2/" + membershiptype + "/Account/" + membershipId + "/Character/" + hunterid + "/Stats/Activities/?count=5&mode=5&page=0", headers=HEADERS)
        history = history.json()
        history_response = history['Response']
        history_activities = history_response['activities']
        match = history_activities[2]
        match_stats = match['values']
        assists = match_stats['assists']
        assists = assists['basic']
        assists = assists['value']
        kills = match_stats['kills']
        kills = kills['basic']
        kills = kills['value']
        deaths = match_stats['deaths']
        deaths = deaths['basic']
        deaths = deaths['value']
        KDA =  match_stats['killsDeathsAssists']
        KDA = KDA['basic']
        KDA = KDA['value']
        score = match_stats['score']
        score = score['basic']
        score = score['value']
        print("\n \nScore: ", score)
        print("Kills: ", kills)
        print("Deaths: ", deaths)
        print("Assists: ", assists)
        print("KDA: :", KDA)
        print("\n \n")
        Hunter_Crucible_History()

    elif Crucible_History_Menu == "4":
        history = requests.get("https://www.bungie.net/Platform/Destiny2/" + membershiptype + "/Account/" + membershipId + "/Character/" + hunterid + "/Stats/Activities/?count=5&mode=5&page=0", headers=HEADERS)
        history = history.json()
        history_response = history['Response']
        history_activities = history_response['activities']
        match = history_activities[3]
        match_stats = match['values']
        assists = match_stats['assists']
        assists = assists['basic']
        assists = assists['value']
        kills = match_stats['kills']
        kills = kills['basic']
        kills = kills['value']
        deaths = match_stats['deaths']
        deaths = deaths['basic']
        deaths = deaths['value']
        KDA =  match_stats['killsDeathsAssists']
        KDA = KDA['basic']
        KDA = KDA['value']
        score = match_stats['score']
        score = score['basic']
        score = score['value']
        print("\n \nScore: ", score)
        print("Kills: ", kills)
        print("Deaths: ", deaths)
        print("Assists: ", assists)
        print("KDA: :", KDA)
        print("\n \n")
        Hunter_Crucible_History() 

    elif Crucible_History_Menu == "5":
        history = requests.get("https://www.bungie.net/Platform/Destiny2/" + membershiptype + "/Account/" + membershipId + "/Character/" + hunterid + "/Stats/Activities/?count=5&mode=5&page=0", headers=HEADERS)
        history = history.json()
        history_response = history['Response']
        history_activities = history_response['activities']
        match = history_activities[4]
        match_stats = match['values']
        assists = match_stats['assists']
        assists = assists['basic']
        assists = assists['value']
        kills = match_stats['kills']
        kills = kills['basic']
        kills = kills['value']
        deaths = match_stats['deaths']
        deaths = deaths['basic']
        deaths = deaths['value']
        KDA =  match_stats['killsDeathsAssists']
        KDA = KDA['basic']
        KDA = KDA['value']
        score = match_stats['score']
        score = score['basic']
        score = score['value']
        print("\n \nScore: ", score)
        print("Kills: ", kills)
        print("Deaths: ", deaths)
        print("Assists: ", assists)
        print("KDA: :", KDA)
        print("\n \n")
        Hunter_Crucible_History()

    elif Crucible_History_Menu == "6":    
        Crucible_Menu()

    elif Crucible_History_Menu == "7":
        Main_Menu()

    elif Crucible_History_Menu == "8":
        quit()

    else:
        print("\nInvalid Input. Try Again.\n")
        Hunter_Crucible_History()

def Titan_Crucible_History():    
    print("\nTitan Crucible Menu: \n1. Match One\n2. Match Two\n3. Match Three\n4. Match Four\n5. Match Five\n6. Crucible Menu\n7. Main Menu\n8. Quit")
    Crucible_History_Menu = input()
    if Crucible_History_Menu == "1":
        history = requests.get("https://www.bungie.net/Platform/Destiny2/" + membershiptype + "/Account/" + membershipId + "/Character/" + titanid + "/Stats/Activities/?count=5&mode=5&page=0", headers=HEADERS)
        history = history.json()
        history_response = history['Response']
        history_activities = history_response['activities']
        match = history_activities[0]
        match_stats = match['values']
        assists = match_stats['assists']
        assists = assists['basic']
        assists = assists['value']
        kills = match_stats['kills']
        kills = kills['basic']
        kills = kills['value']
        deaths = match_stats['deaths']
        deaths = deaths['basic']
        deaths = deaths['value']
        KDA =  match_stats['killsDeathsAssists']
        KDA = KDA['basic']
        KDA = KDA['value']
        score = match_stats['score']
        score = score['basic']
        score = score['value']
        print("\n \nScore: ", score)
        print("Kills: ", kills)
        print("Deaths: ", deaths)
        print("Assists: ", assists)
        print("KDA: :", KDA)
        print("\n \n")
        Titan_Crucible_History()
        
    elif Crucible_History_Menu == "2":
        history = requests.get("https://www.bungie.net/Platform/Destiny2/" + membershiptype + "/Account/" + membershipId + "/Character/" + titanid + "/Stats/Activities/?count=5&mode=5&page=0", headers=HEADERS)
        history = history.json()
        history_response = history['Response']
        history_activities = history_response['activities']
        match = history_activities[1]
        match_stats = match['values']
        assists = match_stats['assists']
        assists = assists['basic']
        assists = assists['value']
        kills = match_stats['kills']
        kills = kills['basic']
        kills = kills['value']
        deaths = match_stats['deaths']
        deaths = deaths['basic']
        deaths = deaths['value']
        KDA =  match_stats['killsDeathsAssists']
        KDA = KDA['basic']
        KDA = KDA['value']
        score = match_stats['score']
        score = score['basic']
        score = score['value']
        print("\n \nScore: ", score)
        print("Kills: ", kills)
        print("Deaths: ", deaths)
        print("Assists: ", assists)
        print("KDA: :", KDA)
        print("\n \n")
        Titan_Crucible_History()
        
    elif Crucible_History_Menu == "3":
        history = requests.get("https://www.bungie.net/Platform/Destiny2/" + membershiptype + "/Account/" + membershipId + "/Character/" + titanid + "/Stats/Activities/?count=5&mode=5&page=0", headers=HEADERS)
        history = history.json()
        history_response = history['Response']
        history_activities = history_response['activities']
        match = history_activities[2]
        match_stats = match['values']
        assists = match_stats['assists']
        assists = assists['basic']
        assists = assists['value']
        kills = match_stats['kills']
        kills = kills['basic']
        kills = kills['value']
        deaths = match_stats['deaths']
        deaths = deaths['basic']
        deaths = deaths['value']
        KDA =  match_stats['killsDeathsAssists']
        KDA = KDA['basic']
        KDA = KDA['value']
        score = match_stats['score']
        score = score['basic']
        score = score['value']
        print("\n \nScore: ", score)
        print("Kills: ", kills)
        print("Deaths: ", deaths)
        print("Assists: ", assists)
        print("KDA: :", KDA)
        print("\n \n")
        Titan_Crucible_History()

    elif Crucible_History_Menu == "4":
        history = requests.get("https://www.bungie.net/Platform/Destiny2/" + membershiptype + "/Account/" + membershipId + "/Character/" + titanid + "/Stats/Activities/?count=5&mode=5&page=0", headers=HEADERS)
        history = history.json()
        history_response = history['Response']
        history_activities = history_response['activities']
        match = history_activities[3]
        match_stats = match['values']
        assists = match_stats['assists']
        assists = assists['basic']
        assists = assists['value']
        kills = match_stats['kills']
        kills = kills['basic']
        kills = kills['value']
        deaths = match_stats['deaths']
        deaths = deaths['basic']
        deaths = deaths['value']
        KDA =  match_stats['killsDeathsAssists']
        KDA = KDA['basic']
        KDA = KDA['value']
        score = match_stats['score']
        score = score['basic']
        score = score['value']
        print("\n \nScore: ", score)
        print("Kills: ", kills)
        print("Deaths: ", deaths)
        print("Assists: ", assists)
        print("KDA: :", KDA)
        print("\n \n")
        Titan_Crucible_History() 

    elif Crucible_History_Menu == "5":
        history = requests.get("https://www.bungie.net/Platform/Destiny2/" + membershiptype + "/Account/" + membershipId + "/Character/" + titanid + "/Stats/Activities/?count=5&mode=5&page=0", headers=HEADERS)
        history = history.json()
        history_response = history['Response']
        history_activities = history_response['activities']
        match = history_activities[4]
        match_stats = match['values']
        assists = match_stats['assists']
        assists = assists['basic']
        assists = assists['value']
        kills = match_stats['kills']
        kills = kills['basic']
        kills = kills['value']
        deaths = match_stats['deaths']
        deaths = deaths['basic']
        deaths = deaths['value']
        KDA =  match_stats['killsDeathsAssists']
        KDA = KDA['basic']
        KDA = KDA['value']
        score = match_stats['score']
        score = score['basic']
        score = score['value']
        print("\n \nScore: ", score)
        print("Kills: ", kills)
        print("Deaths: ", deaths)
        print("Assists: ", assists)
        print("KDA: :", KDA)
        print("\n \n")
        Titan_Crucible_History()

    elif Crucible_History_Menu == "6":    
        Crucible_Menu()

    elif Crucible_History_Menu == "7":
        Main_Menu()

    elif Crucible_History_Menu == "8":
        quit()

    else:
        print("\nInvalid Input. Try Again.\n")
        Titan_Crucible_History()



def Strike_Menu():
    print("\nStrike Menu: \n1. Warlock\n2. Hunter\n3. Titan\n4. Main Menu\n5. Quit")
    Strike_Menu_Input = input()
    if Strike_Menu_Input == "1":
        Warlock_Strike_History()
    elif Strike_Menu_Input == "2":
        Hunter_Strike_History()
    elif Strike_Menu_Input == "3":
        Titan_Strike_History()
    elif Strike_Menu_Input == "4":
        main()
    elif Strike_Menu_Input == "5":
        quit()
    else:
        print("\nInvalid Input. Try Again.\n")
        Strike_Menu()
#Again, a menu that just calls on functions

def Warlock_Strike_History():
    print("\nWarlock Strike Menu: \n1. Strike One\n2. Strike Two\n3. Strike Three\n4. Strike Four\n5. Strike Five\n6. Strike Menu\n7. Main Menu\n8. Quit")
    Strike_History_Menu = input()
    if Strike_History_Menu == "1":
        history = requests.get("https://www.bungie.net/Platform/Destiny2/" + membershiptype + "/Account/" + membershipId + "/Character/" + warlockid + "/Stats/Activities/?count=5&mode=3&page=0", headers=HEADERS)
        history = history.json()
        strike_stats = history['Response']['activities'][0]['values']
        assists = strike_stats['assists']['basic']['value']
        kills = strike_stats['kills']['basic']['value']
        deaths = strike_stats['deaths']['basic']['value']
        KDA = strike_stats['killsDeathsAssists']['basic']['value']
        length = strike_stats['timePlayedSeconds']['basic']['displayValue']
#I finally learned how to properly sort through a json!  This looks way cleaner than the Crucible section.  Again, sorts through the GET request to find the stats I want.  I then assign them variables so I can have cleaning looking print functions below.        
        
        print("\n \nTime: ", length)
        print("Kills: ", kills)
        print("Deaths: ", deaths)
        print("Assists: ", assists)
        print("KDA: :", KDA)
        print("\n \n")
        Warlock_Strike_History()
   
    elif Strike_History_Menu == "2":
        history = requests.get("https://www.bungie.net/Platform/Destiny2/" + membershiptype + "/Account/" + membershipId + "/Character/" + warlockid + "/Stats/Activities/?count=5&mode=3&page=0", headers=HEADERS)
        history = history.json()
        strike_stats = history['Response']['activities'][1]['values']
        assists = strike_stats['assists']['basic']['value']
        kills = strike_stats['kills']['basic']['value']
        deaths = strike_stats['deaths']['basic']['value']
        KDA = strike_stats['killsDeathsAssists']['basic']['value']
        length = strike_stats['timePlayedSeconds']['basic']['displayValue']
        print("\n \nTime: ", length)
        print("Kills: ", kills)
        print("Deaths: ", deaths)
        print("Assists: ", assists)
        print("KDA: :", KDA)
        print("\n \n")
        Warlock_Strike_History()        
        
    elif Strike_History_Menu == "3":
        history = requests.get("https://www.bungie.net/Platform/Destiny2/" + membershiptype + "/Account/" + membershipId + "/Character/" + warlockid + "/Stats/Activities/?count=5&mode=3&page=0", headers=HEADERS)
        history = history.json()
        strike_stats = history['Response']['activities'][2]['values']
        assists = strike_stats['assists']['basic']['value']
        kills = strike_stats['kills']['basic']['value']
        deaths = strike_stats['deaths']['basic']['value']
        KDA = strike_stats['killsDeathsAssists']['basic']['value']
        length = strike_stats['timePlayedSeconds']['basic']['displayValue']
        print("\n \nTime: ", length)
        print("Kills: ", kills)
        print("Deaths: ", deaths)
        print("Assists: ", assists)
        print("KDA: :", KDA)
        print("\n \n")
        Warlock_Strike_History()

    elif Strike_History_Menu == "4":
        history = requests.get("https://www.bungie.net/Platform/Destiny2/" + membershiptype + "/Account/" + membershipId + "/Character/" + warlockid + "/Stats/Activities/?count=5&mode=3&page=0", headers=HEADERS)
        history = history.json()
        strike_stats = history['Response']['activities'][3]['values']
        assists = strike_stats['assists']['basic']['value']
        kills = strike_stats['kills']['basic']['value']
        deaths = strike_stats['deaths']['basic']['value']
        KDA = strike_stats['killsDeathsAssists']['basic']['value']
        length = strike_stats['timePlayedSeconds']['basic']['displayValue']
        print("\n \nTime: ", length)
        print("Kills: ", kills)
        print("Deaths: ", deaths)
        print("Assists: ", assists)
        print("KDA: :", KDA)
        print("\n \n")
        Warlock_Strike_History()
        
    elif Strike_History_Menu == "5":
        history = requests.get("https://www.bungie.net/Platform/Destiny2/" + membershiptype + "/Account/" + membershipId + "/Character/" + warlockid + "/Stats/Activities/?count=5&mode=3&page=0", headers=HEADERS)
        history = history.json()
        strike_stats = history['Response']['activities'][4]['values']
        assists = strike_stats['assists']['basic']['value']
        kills = strike_stats['kills']['basic']['value']
        deaths = strike_stats['deaths']['basic']['value']
        KDA = strike_stats['killsDeathsAssists']['basic']['value']
        length = strike_stats['timePlayedSeconds']['basic']['displayValue']
        print("\n \nTime: ", length)
        print("Kills: ", kills)
        print("Deaths: ", deaths)
        print("Assists: ", assists)
        print("KDA: :", KDA)
        print("\n \n")
        Warlock_Strike_History()

    elif Strike_History_Menu == "6":
        Strike_Menu()

    elif Strike_History_Menu == "7":
        Main_Menu()

    elif Strike_History_Menu == "8":
        quit()
    
    else:
        print("\nInvalid Input. Try Again.\n")
        Warlock_Strike_History()
#The other Character's Menus are exactly the same, save for using their specific ID in the GET Request.  I could probably figure out a way to make this 1 function, but I'll pass.


def Hunter_Strike_History():
    print("\nHunter Strike Menu: \n1. Strike One\n2. Strike Two\n3. Strike Three\n4. Strike Four\n5. Strike Five\n6. Strike Menu\n7. Main Menu\n8. Quit")
    Strike_History_Menu = input()
    if Strike_History_Menu == "1":
        history = requests.get("https://www.bungie.net/Platform/Destiny2/" + membershiptype + "/Account/" + membershipId + "/Character/" + hunterid + "/Stats/Activities/?count=5&mode=3&page=0", headers=HEADERS)
        history = history.json()
        strike_stats = history['Response']['activities'][0]['values']
        assists = strike_stats['assists']['basic']['value']
        kills = strike_stats['kills']['basic']['value']
        deaths = strike_stats['deaths']['basic']['value']
        KDA = strike_stats['killsDeathsAssists']['basic']['value']
        length = strike_stats['timePlayedSeconds']['basic']['displayValue']
        print("\n \nTime: ", length)
        print("Kills: ", kills)
        print("Deaths: ", deaths)
        print("Assists: ", assists)
        print("KDA: :", KDA)
        print("\n \n")
        Hunter_Strike_History()
   
    elif Strike_History_Menu == "2":
        history = requests.get("https://www.bungie.net/Platform/Destiny2/" + membershiptype + "/Account/" + membershipId + "/Character/" + hunterid + "/Stats/Activities/?count=5&mode=3&page=0", headers=HEADERS)
        history = history.json()
        strike_stats = history['Response']['activities'][1]['values']
        assists = strike_stats['assists']['basic']['value']
        kills = strike_stats['kills']['basic']['value']
        deaths = strike_stats['deaths']['basic']['value']
        KDA = strike_stats['killsDeathsAssists']['basic']['value']
        length = strike_stats['timePlayedSeconds']['basic']['displayValue']
        print("\n \nTime: ", length)
        print("Kills: ", kills)
        print("Deaths: ", deaths)
        print("Assists: ", assists)
        print("KDA: :", KDA)
        print("\n \n")
        Hunter_Strike_History()        
        
    elif Strike_History_Menu == "3":
        history = requests.get("https://www.bungie.net/Platform/Destiny2/" + membershiptype + "/Account/" + membershipId + "/Character/" + hunterid + "/Stats/Activities/?count=5&mode=3&page=0", headers=HEADERS)
        history = history.json()
        strike_stats = history['Response']['activities'][2]['values']
        assists = strike_stats['assists']['basic']['value']
        kills = strike_stats['kills']['basic']['value']
        deaths = strike_stats['deaths']['basic']['value']
        KDA = strike_stats['killsDeathsAssists']['basic']['value']
        length = strike_stats['timePlayedSeconds']['basic']['displayValue']
        print("\n \nTime: ", length)
        print("Kills: ", kills)
        print("Deaths: ", deaths)
        print("Assists: ", assists)
        print("KDA: :", KDA)
        print("\n \n")
        Hunter_Strike_History()

    elif Strike_History_Menu == "4":
        history = requests.get("https://www.bungie.net/Platform/Destiny2/" + membershiptype + "/Account/" + membershipId + "/Character/" + warlockid + "/Stats/Activities/?count=5&mode=3&page=0", headers=HEADERS)
        history = history.json()
        strike_stats = history['Response']['activities'][3]['values']
        assists = strike_stats['assists']['basic']['value']
        kills = strike_stats['kills']['basic']['value']
        deaths = strike_stats['deaths']['basic']['value']
        KDA = strike_stats['killsDeathsAssists']['basic']['value']
        length = strike_stats['timePlayedSeconds']['basic']['displayValue']
        print("\n \nTime: ", length)
        print("Kills: ", kills)
        print("Deaths: ", deaths)
        print("Assists: ", assists)
        print("KDA: :", KDA)
        print("\n \n")
        Hunter_Strike_History()
        
    elif Strike_History_Menu == "5":
        history = requests.get("https://www.bungie.net/Platform/Destiny2/" + membershiptype + "/Account/" + membershipId + "/Character/" + hunterid + "/Stats/Activities/?count=5&mode=3&page=0", headers=HEADERS)
        history = history.json()
        strike_stats = history['Response']['activities'][4]['values']
        assists = strike_stats['assists']['basic']['value']
        kills = strike_stats['kills']['basic']['value']
        deaths = strike_stats['deaths']['basic']['value']
        KDA = strike_stats['killsDeathsAssists']['basic']['value']
        length = strike_stats['timePlayedSeconds']['basic']['displayValue']
        print("\n \nTime: ", length)
        print("Kills: ", kills)
        print("Deaths: ", deaths)
        print("Assists: ", assists)
        print("KDA: :", KDA)
        print("\n \n")
        Hunter_Strike_History()

    elif Strike_History_Menu == "6":
        Strike_Menu()

    elif Strike_History_Menu == "7":
        Main_Menu()

    elif Strike_History_Menu == "8":
        quit()
    
    else:
        print("\nInvalid Input. Try Again.\n")
        Hunter_Strike_History()

def Titan_Strike_History():
    print("\n Titan Strike Menu: \n1. Strike One\n2. Strike Two\n3. Strike Three\n4. Strike Four\n5. Strike Five\n6. Strike Menu\n7. Main Menu\n8. Quit")
    Strike_History_Menu = input()
    if Strike_History_Menu == "1":
        history = requests.get("https://www.bungie.net/Platform/Destiny2/" + membershiptype + "/Account/" + membershipId + "/Character/" + titanid + "/Stats/Activities/?count=5&mode=3&page=0", headers=HEADERS)
        history = history.json()
        strike_stats = history['Response']['activities'][0]['values']
        assists = strike_stats['assists']['basic']['value']
        kills = strike_stats['kills']['basic']['value']
        deaths = strike_stats['deaths']['basic']['value']
        KDA = strike_stats['killsDeathsAssists']['basic']['value']
        length = strike_stats['timePlayedSeconds']['basic']['displayValue']
        print("\n \nTime: ", length)
        print("Kills: ", kills)
        print("Deaths: ", deaths)
        print("Assists: ", assists)
        print("KDA: :", KDA)
        print("\n \n")
        Titan_Strike_History()
   
    elif Strike_History_Menu == "2":
        history = requests.get("https://www.bungie.net/Platform/Destiny2/" + membershiptype + "/Account/" + membershipId + "/Character/" + titanid + "/Stats/Activities/?count=5&mode=3&page=0", headers=HEADERS)
        history = history.json()
        strike_stats = history['Response']['activities'][1]['values']
        assists = strike_stats['assists']['basic']['value']
        kills = strike_stats['kills']['basic']['value']
        deaths = strike_stats['deaths']['basic']['value']
        KDA = strike_stats['killsDeathsAssists']['basic']['value']
        length = strike_stats['timePlayedSeconds']['basic']['displayValue']
        print("\n \nTime: ", length)
        print("Kills: ", kills)
        print("Deaths: ", deaths)
        print("Assists: ", assists)
        print("KDA: :", KDA)
        print("\n \n")
        Titan_Strike_History()        
        
    elif Strike_History_Menu == "3":
        history = requests.get("https://www.bungie.net/Platform/Destiny2/" + membershiptype + "/Account/" + membershipId + "/Character/" + titanid + "/Stats/Activities/?count=5&mode=3&page=0", headers=HEADERS)
        history = history.json()
        strike_stats = history['Response']['activities'][2]['values']
        assists = strike_stats['assists']['basic']['value']
        kills = strike_stats['kills']['basic']['value']
        deaths = strike_stats['deaths']['basic']['value']
        KDA = strike_stats['killsDeathsAssists']['basic']['value']
        length = strike_stats['timePlayedSeconds']['basic']['displayValue']
        print("\n \nTime: ", length)
        print("Kills: ", kills)
        print("Deaths: ", deaths)
        print("Assists: ", assists)
        print("KDA: :", KDA)
        print("\n \n")
        Titan_Strike_History()

    elif Strike_History_Menu == "4":
        history = requests.get("https://www.bungie.net/Platform/Destiny2/" + membershiptype + "/Account/" + membershipId + "/Character/" + titanid + "/Stats/Activities/?count=5&mode=3&page=0", headers=HEADERS)
        history = history.json()
        strike_stats = history['Response']['activities'][3]['values']
        assists = strike_stats['assists']['basic']['value']
        kills = strike_stats['kills']['basic']['value']
        deaths = strike_stats['deaths']['basic']['value']
        KDA = strike_stats['killsDeathsAssists']['basic']['value']
        length = strike_stats['timePlayedSeconds']['basic']['displayValue']
        print("\n \nTime: ", length)
        print("Kills: ", kills)
        print("Deaths: ", deaths)
        print("Assists: ", assists)
        print("KDA: :", KDA)
        print("\n \n")
        Titan_Strike_History()
        
    elif Strike_History_Menu == "5":
        history = requests.get("https://www.bungie.net/Platform/Destiny2/" + membershiptype + "/Account/" + membershipId + "/Character/" + titanid + "/Stats/Activities/?count=5&mode=3&page=0", headers=HEADERS)
        history = history.json()
        strike_stats = history['Response']['activities'][4]['values']
        assists = strike_stats['assists']['basic']['value']
        kills = strike_stats['kills']['basic']['value']
        deaths = strike_stats['deaths']['basic']['value']
        KDA = strike_stats['killsDeathsAssists']['basic']['value']
        length = strike_stats['timePlayedSeconds']['basic']['displayValue']
        print("\n \nTime: ", length)
        print("Kills: ", kills)
        print("Deaths: ", deaths)
        print("Assists: ", assists)
        print("KDA: :", KDA)
        print("\n \n")
        Titan_Strike_History()

    elif Strike_History_Menu == "6":
        Strike_Menu()

    elif Strike_History_Menu == "7":
        Main_Menu()

    elif Strike_History_Menu == "8":
        quit()
    
    else:
        print("\nInvalid Input. Try Again.\n")
        Titan_Strike_History()

def Clan_Menu():
    print("\nClan Menu:\n1: Crucible Leaderboards\n2: Strike Leaderboards\n3: Raid Leaderboards\n4: Main Menu\n5: Quit\n")
    Clan_Function_Input = input()
    if Clan_Function_Input == "1":
        Clan_Crucible()
    elif Clan_Function_Input == "2":
        Clan_Strikes()
    elif Clan_Function_Input == "3":
        Clan_Raids()
    elif Clan_Function_Input == "4":
        Main_Menu()
    elif Clan_Function_Input == "5":
        quit()
    else:
        print("\n \nInvalid Input. Try Again.\n \n")
        Clan_Menu()

def Clan_Crucible():
    print("\nCrucible Leaderboards:\n1: Kills\n2: Deaths\n3: Assists\n4: Clan Menu\n5: Main Menu\n6: Quit\n")
    Clan_Crucible_Input = input()
    leaderboard = requests.get("https://www.bungie.net/Platform/Destiny2/Stats/Leaderboards/Clans/4228101/?maxtop=5&modes=5", headers=HEADERS)
    leaderboard = leaderboard.json()
    leaderboard = leaderboard['Response']['allPvP']
    if Clan_Crucible_Input == "1":
        kills = leaderboard['lbKills']['entries']
        print("\nKILLS:")
        print("1: ", kills[0]['player']['destinyUserInfo']['displayName'], kills[0]['value']['basic']['value'])
        print("2: ", kills[1]['player']['destinyUserInfo']['displayName'], kills[1]['value']['basic']['value'])
        print("3: ", kills[2]['player']['destinyUserInfo']['displayName'], kills[2]['value']['basic']['value'])
        print("4: ", kills[3]['player']['destinyUserInfo']['displayName'], kills[3]['value']['basic']['value'])
        print("5: ", kills[4]['player']['destinyUserInfo']['displayName'], kills[4]['value']['basic']['value'], "\n")
        Clan_Crucible()
    elif Clan_Crucible_Input == "2":
        deaths = leaderboard['lbDeaths']['entries']
        print("\nDEATHS:")
        print("1: ", deaths[0]['player']['destinyUserInfo']['displayName'], deaths[0]['value']['basic']['value'])
        print("2: ", deaths[1]['player']['destinyUserInfo']['displayName'], deaths[1]['value']['basic']['value'])
        print("3: ", deaths[2]['player']['destinyUserInfo']['displayName'], deaths[2]['value']['basic']['value'])
        print("4: ", deaths[3]['player']['destinyUserInfo']['displayName'], deaths[3]['value']['basic']['value'])
        print("5: ", deaths[4]['player']['destinyUserInfo']['displayName'], deaths[4]['value']['basic']['value'], "\n")
        Clan_Crucible()
    elif Clan_Crucible_Input == "3":
        assists = leaderboard['lbAssists']['entries']
        print("\nASSISTS:")
        print("1: ", assists[0]['player']['destinyUserInfo']['displayName'], assists[0]['value']['basic']['value'])
        print("2: ", assists[1]['player']['destinyUserInfo']['displayName'], assists[1]['value']['basic']['value'])
        print("3: ", assists[2]['player']['destinyUserInfo']['displayName'], assists[2]['value']['basic']['value'])
        print("4: ", assists[3]['player']['destinyUserInfo']['displayName'], assists[3]['value']['basic']['value'])
        print("5: ", assists[4]['player']['destinyUserInfo']['displayName'], assists[4]['value']['basic']['value'], "\n")
        Clan_Crucible()
    elif Clan_Crucible_Input == "4":
        Clan_Menu()
    elif Clan_Crucible_Input == "5":
        Main_Menu()
    elif Clan_Crucible_Input == "6":
        quit()
    else: 
        print("\nInvalid Input. Try Again.\n")
        Clan_Crucible()


def Clan_Strikes():
    print("\nStrike Leaderboards:\n1: Kills\n2: Deaths\n3: Assists\n4: Clan Menu\n5: Main Menu\n6: Quit\n")
    Clan_Strikes_Input = input()
    leaderboard = requests.get("https://www.bungie.net/Platform/Destiny2/Stats/Leaderboards/Clans/4228101/?maxtop=5&modes=3", headers=HEADERS)
    leaderboard = leaderboard.json()
    leaderboard = leaderboard['Response']['strike']
    if Clan_Strikes_Input == "1":
        kills = leaderboard['lbKills']['entries']
        print("\nKILLS:")
        print("1: ", kills[0]['player']['destinyUserInfo']['displayName'], kills[0]['value']['basic']['value'])
        print("2: ", kills[1]['player']['destinyUserInfo']['displayName'], kills[1]['value']['basic']['value'])
        print("3: ", kills[2]['player']['destinyUserInfo']['displayName'], kills[2]['value']['basic']['value'])
        print("4: ", kills[3]['player']['destinyUserInfo']['displayName'], kills[3]['value']['basic']['value'])
        print("5: ", kills[4]['player']['destinyUserInfo']['displayName'], kills[4]['value']['basic']['value'], "\n")
        Clan_Strikes()
    elif Clan_Strikes_Input == "2":
        deaths = leaderboard['lbDeaths']['entries']
        print("\nDEATHS:")
        print("1: ", deaths[0]['player']['destinyUserInfo']['displayName'], deaths[0]['value']['basic']['value'])
        print("2: ", deaths[1]['player']['destinyUserInfo']['displayName'], deaths[1]['value']['basic']['value'])
        print("3: ", deaths[2]['player']['destinyUserInfo']['displayName'], deaths[2]['value']['basic']['value'])
        print("4: ", deaths[3]['player']['destinyUserInfo']['displayName'], deaths[3]['value']['basic']['value'])
        print("5: ", deaths[4]['player']['destinyUserInfo']['displayName'], deaths[4]['value']['basic']['value'], "\n")
        Clan_Strikes()
    elif Clan_Strikes_Input == "3":
        assists = leaderboard['lbAssists']['entries']
        print("\nASSISTS:")
        print("1: ", assists[0]['player']['destinyUserInfo']['displayName'], assists[0]['value']['basic']['value'])
        print("2: ", assists[1]['player']['destinyUserInfo']['displayName'], assists[1]['value']['basic']['value'])
        print("3: ", assists[2]['player']['destinyUserInfo']['displayName'], assists[2]['value']['basic']['value'])
        print("4: ", assists[3]['player']['destinyUserInfo']['displayName'], assists[3]['value']['basic']['value'])
        print("5: ", assists[4]['player']['destinyUserInfo']['displayName'], assists[4]['value']['basic']['value'], "\n")
        Clan_Strikes()
    elif Clan_Strikes_Input == "4":
        Clan_Menu()
    elif Clan_Strikes_Input == "5":
        Main_Menu()
    elif Clan_Strikes_Input == "6":
        quit()
    else:
        print("\nInvalid Input. Try Again.\n")
        Clan_Strikes()


def Clan_Raids():
    print("\nRaid Leaderboards:\n1: Kills\n2: Deaths\n3: Assists\n4: Clan Menu\n5: Main Menu\n6: Quit\n")
    Clan_Raids_Input = input()
    leaderboard = requests.get("https://www.bungie.net/Platform/Destiny2/Stats/Leaderboards/Clans/4228101/?maxtop=5&modes=4", headers=HEADERS)
    leaderboard = leaderboard.json()
    leaderboard = leaderboard['Response']['raid']
    if Clan_Raids_Input == "1":
        kills = leaderboard['lbKills']['entries']
        print("\nKILLS:")
        print("1: ", kills[0]['player']['destinyUserInfo']['displayName'], kills[0]['value']['basic']['value'])
        print("2: ", kills[1]['player']['destinyUserInfo']['displayName'], kills[1]['value']['basic']['value'])
        print("3: ", kills[2]['player']['destinyUserInfo']['displayName'], kills[2]['value']['basic']['value'])
        print("4: ", kills[3]['player']['destinyUserInfo']['displayName'], kills[3]['value']['basic']['value'])
        print("5: ", kills[4]['player']['destinyUserInfo']['displayName'], kills[4]['value']['basic']['value'], "\n")
        Clan_Raids()
    elif Clan_Raids_Input == "2":
        deaths = leaderboard['lbDeaths']['entries']
        print("\nDEATHS:")
        print("1: ", deaths[0]['player']['destinyUserInfo']['displayName'], deaths[0]['value']['basic']['value'])
        print("2: ", deaths[1]['player']['destinyUserInfo']['displayName'], deaths[1]['value']['basic']['value'])
        print("3: ", deaths[2]['player']['destinyUserInfo']['displayName'], deaths[2]['value']['basic']['value'])
        print("4: ", deaths[3]['player']['destinyUserInfo']['displayName'], deaths[3]['value']['basic']['value'])
        print("5: ", deaths[4]['player']['destinyUserInfo']['displayName'], deaths[4]['value']['basic']['value'], "\n")
        Clan_Raids()
    elif Clan_Raids_Input == "3":
        assists = leaderboard['lbAssists']['entries']
        print("\nASSISTS:")
        print("1: ", assists[0]['player']['destinyUserInfo']['displayName'], assists[0]['value']['basic']['value'])
        print("2: ", assists[1]['player']['destinyUserInfo']['displayName'], assists[1]['value']['basic']['value'])
        print("3: ", assists[2]['player']['destinyUserInfo']['displayName'], assists[2]['value']['basic']['value'])
        print("4: ", assists[3]['player']['destinyUserInfo']['displayName'], assists[3]['value']['basic']['value'])
        print("5: ", assists[4]['player']['destinyUserInfo']['displayName'], assists[4]['value']['basic']['value'], "\n")
        Clan_Raids()
    elif Clan_Raids_Input == "4":
        Clan_Menu()
    elif Clan_Raids_Input == "5":
        Main_Menu()
    elif Clan_Raids_Input == "6":
        quit()
    else:
        print("\nInvalid Input. Try Again.\n")
        Clan_Raids()




Main_Menu()
#Call the Main_Menu function to start the script
