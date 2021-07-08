#!/usr/bin/env python3

import requests
import json
import time

HEADERS = {"X-API-Key":'c6b881de35a143f98cda3d1e5dbf27b4'}
X_API_Key = 'c6b881de35a143f98cda3d1e5dbf27b4'
user_name = input("Username:")
user_platform = input("Platform. xbox=1, psn=2, pc=4")
components = "200"
base_url = 'https://bungie.net/Platform/Destiny2/'

#def get_user_id(user_name, user_platform, X_API_Key):
userprofile = requests.get(base_url + 'SearchDestinyPlayer/' + user_platform + '/' + user_name, headers=HEADERS);
userprofile = userprofile.json()
response1 = userprofile['Response']
data1 = response1[0]
membershipId = data1['membershipId']

characters_list = requests.get(base_url + user_platform + '/' + 'Profile/' + membershipId + '/?components=200', headers=HEADERS);
characters_list = characters_list.json()
#character_list = print(characters)
response2 = characters_list['Response']
characters = response2['characters']
data2 = characters['data']
warlock = data2['2305843009291236579']
print(warlock)
#print(characters)
#print(membershipId)
