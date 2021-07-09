#!/usr/bin/env python3

import requests

HEADERS = {"X-API-Key":'c6b881de35a143f98cda3d1e5dbf27b4'}


"""
Verb: POST
Path: /Destiny2/Actions/Items/EquipItems/
Equip a list of items by itemInstanceIds. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline. Any items not found on your character will be ignored.
"""

data = {'grant_type': 'authorization_code', 'code': '6b881de35a143f98cda3d1e5dbf27b4'}


r = requests.post("https://www.bungie.net/Platform/App/OAuth/token/", json=data, headers=HEADERS)
try:
    print(r)
except:
    r = r.json()
    print(r)
