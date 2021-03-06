#!/usr/bin/env python3

import flask
from flask import current_app, url_for, request, redirect, session
import requests
from urllib import parse

import json

class OAuthSignin(object):
    providers = None

    def __init__(self, provider_name):
        super().__init__()
        self.provider_name = provider_name
        credentials = current_app.config['OAUTH_CREDENTIALS'][provider_name]
        self.consumer_id        = credentials['37057']
        self.consumer_secret    = credentials['bdOqDW-9po.QSWkwiHOpyA9HTN2vSwbP3PNy35pDuZc']
        self.api_key            = credentials['c6b881de35a143f98cda3d1e5dbf27b4']

    def authorize(self):
        pass

    def callback(self):
        pass

    def save_created_state(self):
        pass

    def make_state_parameter(self):
        pass

    def is_valid_state(self):
        pass

    def get_callback_url(self):
        return url_for('oauth_callback', provider=self.provider_name, _external=True)

    @classmethod
    def get_provider(cls, provider_name):
        if cls.providers is None:
            cls.providers = {}
            for provider_class in cls.__subclasses__():
                provider = provider_class()
                cls.providers[provider.provider_name] = provider
        return cls.providers[provider_name]
        # if self.providers is None:
        #     self.providers = {}
        #     for provider_class in self.__subclasses__():
        #         provider = provider_class()
        #         self.providers[provider.provider_name] = provider
        # return self.providers[provider_name]

class BungieSignIn(OAuthSignin):
    def __init__(self):
        super(BungieSignIn, self).__init__('bungie')
        # TODO: Maybe replace?
        self.service = {
            'name'              : 'bungie',
            'client_id'         : self.consumer_id,
            'client_secret'     : self.consumer_secret,
            'api_key'           : self.api_key,
            'authorize_url'     : 'https://www.bungie.net/en/oauth/authorize?',
            'access_token_url'  : 'https://www.bungie.net/platform/app/oauth/token/',
            'base_url'          : 'https://www.bungie.com/',
            'headers'           : {'X-API-Key':self.api_key}
        }
        self.headers= {'X-API-Key':self.api_key}

    def authorize(self):
        my_state=self.make_state_parameter()
        url_params = {
            'client_id': self.service['client_id'],
            'response_type': 'code',
            'state': my_state
            }
        auth_url = self.service['authorize_url'] + parse.urlencode(url_params)
        return redirect(auth_url)


    def get_callback_url(self):
        """
        1) Recieve the authorization code from Bungie.
        2) Request the access token.
        3) Returns a dict with auth headers.
        """
        if 'code' not in request.args:
            print("No code...")
            return None
        if not 'state' in request.args:
            print("No CSRF state parameter - unknown user.")
            return False

        code = request.args['code']
        state = request.args['state']
        return_state_matches = self.is_valid_state(state)
        if not return_state_matches:
            print("Unknown user accessing.")
            return None

        headers = self.service['headers']
        headers['Content-Type']		= 'application/x-www-form-urlencoded'
        headers['client_id'] 		= self.service['client_id']
        headers['client_secret']	= self.service['client_secret']

        post_data = f'grant_type=authorization_code&code={code}&client_id={self.service["client_id"]}&client_secret={self.service["client_secret"]}'
        response = requests.post(self.service['access_token_url'], data=post_data, headers=headers)

        # Useful debug print statements:
        # print(response.status_code)
        # print(response.text)
        # print(response.json())

        token_json              = response.json()['access_token']
        membership_id           = response.json()["membership_id"]
        headers["X-API-Key"]    = self.service['api_key']
        headers["Authorization"] = 'Bearer ' + str(token_json)
        headers["membership_id"] = str(membership_id)
        print(token_json)
        return headers


    # Save state parameter used in CSRF protection:
    def save_created_state(self, state):
        """
        Save the state parameter used in CSRF protection.
        """
        session['state_token'] = state
        pass

    def make_state_parameter(self):
        """ Generate a random string for the state parameter
        Save it for use later to prevent xsrf attacks """
        from uuid import uuid4
        state = str(uuid4())
        self.save_created_state(state)
        return state

    def is_valid_state(self, state):
        saved_state = session['state_token']
        if state == saved_state:
            return True
        else:
            return False

