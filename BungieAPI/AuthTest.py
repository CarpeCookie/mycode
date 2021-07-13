#!/usr/bin/env python3

import requests
import json

HEADERS = {"X-API-Key":"c6b881de35a143f98cda3d1e5dbf27b4"}
try:    
    response = requests.get("https://www.bungie.net/en/OAuth/Authorize?client_id=37057&response_type=code&state=bdOqDW-9po.QSWkwiHOpyA9HTN2vSwbP3PNy35pDuZc", headers=HEADERS)    
    
    with open("AuthResponse.txt", "w") as f:
        print(response)
        try:
            print(response.text)
        except:
            print("partial Failure")
except:
    print("failure")
