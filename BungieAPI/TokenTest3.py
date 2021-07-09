#!/usr/bin/env python3
from rauth import OAuth2Service

bungie =  OAuth2Service(
    client_id='c6b881de35a143f98cda3d1e5dbf27b4',
    client_secret='bdOqDW-9po.QSWkwiHOpyA9HTN2vSwbP3PNy35pDuZc',
    name='bungie',
    access_token_url='https://www.bungie.net/Platform/App/OAuth/token/',
    authorize_url='https://www.bungie.net/Platform/App/OAuth/Authorize',   
    base_url='https://www.bungie.net/Platform'
    )
print(bungie)


