#!/usr/bin/env python3

import json
import requests
from rauth import OAuth2Service

class ExampleOAuth2Client:
     def __init__(self, client_id, client_secret):
         self.access_token = None

         self.service = OAuth2Service(
            name="foo",
            client_id=37057,
            client_secret="bdOqDW-9po.QSWkwiHOpyA9HTN2vSwbP3PNy35pDuZc",
            access_token_url="https://www.bungie.net/Platform/App/OAuth/token/",
            authorize_url="https://www.bungie.net/en/OAuth/Authorize",
            base_url="https://www.bungie.net/Platform",
            )   

         self.get_access_token()

     def get_access_token(self):
        data = {'code': '91a212db9f3a7cb8ed96348f73237ca5',
                'grant_type': 'authorization_code',
                'redirect_uri': 'https://www.bungie.net/en/OAuth/Authorize?client_id=37057&response_type=code&state=bdOqDW-9po.QSWkwiHOpyA9HTN2vSwbP3PNy35pDuZc'}

        session = self.service.get_auth_session(data=data, decoder=json.loads)

        self.access_token = session.access_token
        print(access_token)
