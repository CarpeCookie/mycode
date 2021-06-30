#!/usr/bin/env python3
loginfail = 0
with open("keystone.common.wsgi", "r") as login:
    for failed in login:
        if "- - - -] Authorization failed" in failed:
            loginfail += 1
    print("Failed log in attempts =", loginfail)
