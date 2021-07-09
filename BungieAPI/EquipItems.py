#!/usr/bin/env python3

import requests
import json 

HEADERS = {"X-API-Key":'c6b881de35a143f98cda3d1e5dbf27b4'}

"""
Verb: POST
Path: /Destiny2/Actions/Items/EquipItems/
Equip a list of items by itemInstanceIds. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline. Any items not found on your character will be ignored.
"""

text_equip_item = {
"itemId": 6917529368069022675,
"characterId": 4611686018465168592,
"membershipType": 2
}

equip_payload = json.dumps(text_equip_item)

try:
    r = session.post("https://www.bungie.net/platform/Destiny2/Actions/Items/EquipItem/", data=equip_payload, headers=HEADERS)
    print("success")
except:
    print("failure")
