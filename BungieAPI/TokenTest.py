#!/usr/bin/env python3

import requests
import json
import time


"""
Verb: POST
Path: /Destiny2/Actions/Items/EquipItems/
Equip a list of items by itemInstanceIds. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline. Any items not found on your character will be ignored.
"""

#data= {
#"grant_type": 'authorization_code',
#"code": '6b881de35a143f98cda3d1e5dbf27b4'
#}

try:
    token = print("https://www.bungie.net/Platform/App/OAuth/token/grant_type=authorization_code&client_id=37057&client_secret=bdOqDW-9po.QSWkwiHOpyA9HTN2vSwbP3PNy35pDuZc").json()["access_token"]
    print(token)
except:
    print("Failure")
