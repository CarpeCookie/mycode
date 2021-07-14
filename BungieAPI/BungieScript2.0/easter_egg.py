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



def Check_Fashion():
    print("\nHow's your fashion sense?\n1: Warlock\n2: Hunter\n3: Titan\n4: Equipment Menu\n5: Main Menu\n6: Quit\n")
    Fashion_Sense = input()
    if Fashion_Sense == "1":
        print("\nYour look could use some work.\n")
        Check_Fashion()
    if Fashion_Sense == "2":
        Hunter_Fashion()
    if Fashion_Sense == "3":
        Titan_Fashion()
    if Fashion_Sense == "4":
        Equipment_Menu()
    if Fashion_Sense == "5":
        Main_Menu()
    elif Fashion_Sense == "6":
        quit()
    else:
        print("\n \nInvalid Input. Try Again.\n \n")
        Check_Fashion()

def Hunter_Fashion():    
    gear = requests.get("https://www.bungie.net/Platform/Destiny2/2/Profile/" + membershipId + "/Character/" + hunterid + "/?components=205", headers=HEADERS)
    gear = gear.json()
    gear = gear['Response']['equipment']['data']['items']
    helm = gear[3]['itemInstanceId']
    arms = gear[4]['itemInstanceId']
    chest = gear[5]['itemInstanceId']
    legs = gear[6]['itemInstanceId']
    class_item = gear[7]['itemInstanceId']


    scooby_hat = "6917529211628824139"
    scooby_arms = "6917529211602451858"
    scooby_chest = "6917529211620260636"
    scooby_legs = "6917529211620255407"
    scooby_snack = "6917529194764422250"

    if helm == scooby_hat:
        if arms == scooby_arms:
            if chest == scooby_chest:
                if legs == scooby_legs:
                    if class_item == scooby_snack:
                        print("\nLooks like we've got another mystery on our hands!\n")
                        Check_Fashion()
                    else:
                        print("\nYour look could use some work.\n")
                        Check_Fashion()
                else:
                    print("\nYour look could use some work.\n")
                    Check_Fashion()
            else:
                print("\nYour look could use some work.\n")
                Check_Fashion()
        else:
            print("\nYour look could use some work.\n")
            Check_Fashion()
    else:
        print("\nYour look could use some work.\n")
        Check_Fashion()

def Titan_Fashion():
    gear = requests.get("https://www.bungie.net/Platform/Destiny2/2/Profile/" + membershipId + "/Character/" + titanid + "/?components=205", headers=HEADERS)
    gear = gear.json()
    gear = gear['Response']['equipment']['data']['items']
    helm = gear[3]['itemInstanceId']
    arms = gear[4]['itemInstanceId']
    chest = gear[5]['itemInstanceId']
    legs = gear[6]['itemInstanceId']
    class_item = gear[7]['itemInstanceId']

    ogre_head = "6917529211829354390"
    ogre_arms = "6917529139640021014"
    ogre_chest = "6917529211978348615"
    ogre_legs = "6917529211823664235"
    ogre_onion = "6917529211984649722"

    if helm == ogre_head:
        if arms == ogre_arms:
            if chest == ogre_chest:
                if legs == ogre_legs:
                    if class_item == ogre_onion:
                        print("\nThat'll do, Donkey. That'll do.\n")
                        Check_Fashion()
                    else:
                        print("\nYour look could use some work.\n")
                        Check_Fashion()
                else:
                    print("\nYour look could use some work.\n")
                    Check_Fashion()
            else:
                print("\nYour look could use some work.\n")
                Check_Fashion()
        else:
            print("\nYour look could use some work.\n")
            Check_Fashion()
    else:
        print("\nYour look could use some work.\n")
        Check_Fashion()

Check_Fashion()
