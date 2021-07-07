#!/usr/bin/env python3

import requests
try:
    HEADERS = {"X-API-Key":"c6b881de35a143f98cda3d1e5dbf27b4", "Authorization":"Basic czZCaGRSa3F0MzpnWDFmQmF0M2JW", "Content-Type":"application/x-www-form-urlencoded"}
    requests.get=("https://www.bungie.net/platform/app/oauth/token/ HTTP/1.1")

    grant_type = "authorization_code&codebdOqDW-9po.QSWkwiHOpyA9HTN2vSwbP3PNy35pDuZc"
    print("success")
except:
    print("failure")
