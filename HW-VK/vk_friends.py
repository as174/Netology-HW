# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 09:30:53 2018

@author: AS
"""

import requests

class User():
    
    def __init__(self, token):
        self.token = token
    
    def get_mutual_friends(self, friend_id):
            params = {
                'target_uid': friend_id,
                'access_token': self.token,
                'v': 5.92     
                }
            url = ('https://api.vk.com/method/friends.getMutual?')
            response = requests.get(url, params).json()
            return(response)

token_1 = '91e932eb4cb252f9e6b3e382f1416846d8cd6cfd2e57d1d6f412071df984257e41d49ea76281cf8d8e3f2'
          
me = User(token_1)

print(me.get_mutual_friends(905767))