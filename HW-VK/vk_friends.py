"""
Created on Mon Dec 10 09:30:53 2018

@author: AS
"""

import requests

token = ''

class User():
    
    def __init__(self, id):
        self.id = id
        
    def get_mutual_friends(self, friend_id):
        params = {
                'target_uid': friend_id,
                'access_token': token,
                'v': 5.92     
           }
        url = ('https://api.vk.com/method/friends.getMutual?')
        response = requests.get(url, params).json()
        return(response)
    
    def __and__(self, other):
        params = {
                'target_uid': other.id,
                'access_token': token,
                'v': 5.92     
                }
        url = ('https://api.vk.com/method/friends.getMutual?')
        response = requests.get(url, params).json()
#        return(response)
        list_id = response['response']
        users = []
        for id in list_id:
            users.append(User(id))
        return(users)
        
    def __str__(self):
        return('https://www.vk.com/id' + str(self.id))
          
me = User(1306975)

friend = User(905767)

print(me)

#friend_2 = User(1029178)
#
#friend_3 = User(6244347)
#
#print(me)