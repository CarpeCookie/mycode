#!/usr/bin/env python3

import requests
HEADERS = {"X-API-Key":"c6b881de35a143f98cda3d1e5dbf27b4"}
try:    
    r = requests.get("https://www.bungie.net/en/OAuth/Authorize?client_id=37057&response_type=code&state=bdOqDW-9po.QSWkwiHOpyA9HTN2vSwbP3PNy35pDuZc", headers=HEADERS)    
    x = r.text
    print(x)
    with open("test.txt", "a") as test: 
        print(x, file=test)

except:
    print("failure")
