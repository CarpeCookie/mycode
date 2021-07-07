#!/usr/bin/env python3

import requests
import json

X-API-Key = c6b881de35a143f98cda3d1e5dbf27b4
user_name = input("Username:")
user_platform = input("Platform. xbox=1, psn=2, pc=4")
components = "200"
base_url = 'https://bungie.net/Platform/Destiny2/'

get_profile_url(user_name, user_platform, componets, X-API-Key):
    user_id = get_user_id(user_name, user_platform, X-API-Key)
    membership_type = user_platform
    componets = '200,300'
    return baseurl + membership_type + '/' + 'Proflie/' + user_id + '/?components=' + components
