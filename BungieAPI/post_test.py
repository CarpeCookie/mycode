#!/usr/bin/env python3

import requests

HEADERS = {"X-API-Key":'c6b881de35a143f98cda3d1e5dbf27b4'}
def main():
    r = requests.get("https://www.bungie.net/Platform/Destiny2/SearchDestinyPlayer/2/CarpeCookie", headers=HEADERS);
# we do this request to pull user profile information.

    userprofile = r.json()    
#the dictiontary its placed into

    response = userprofile['Response']
    data = response[0]
    membershipId = data['membershipId']
#breaking down the dictionary since I don't know how to search the subsections with a string.  I'll likely be using the membershipId often, so I just assigned it its own name.  I won't have to keep using a command to pull it from the list.  Also, the name of the value will be the same as the API I'm pulling from, making it easier to understand.
    print(membershipId)
main()
