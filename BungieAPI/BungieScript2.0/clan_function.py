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
