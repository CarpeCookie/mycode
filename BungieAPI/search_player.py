#!/usr/bin/env python3

import requests

BungieAPI = 'https://www.bungie.net'
ProfileSearch = '/Platform/Destiny2/SearchDestinyPlayer/2/CarpeCookie'

def main():
    try:
        userprofile = requests.get(BungieAPI + ProfileSearch)
        print(userprofile)
    except:
        print("failure")
main()
