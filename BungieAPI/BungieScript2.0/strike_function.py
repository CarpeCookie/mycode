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
        Main_Menu()
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

Main_Menu()

