# -*- coding: utf-8 -*-
"""

@author: AS
"""

import requests
import time
import json

token  = 'ed1271af9e8883f7a7c2cefbfddfcbc61563029666c487b2f71a5227cce0d1b533c4af4c5b888633c06ae'



#user_name = 'eshmargunov'
#
#user_id = 171691064

user = input('Введите id пользователя или его user_name:')

def find_user_id(user):
    try: 
        params = {
                'access_token': token,
                'v': 5.92,
                'q': user
                }
        url = 'https://api.vk.com/method/users.search' 
        response = requests.get(url, params=params, timeout=30).json()
        user_id = response['response']['items'][0]['id']
    except:
        user_id = user
    return(user_id)


def get_user_groups():
    user_id = find_user_id(user)
    params = {
        'access_token': token,
        'v': 5.92,
        'user_ids': user_id
        }
    url = 'https://api.vk.com/method/groups.get' 
    response = requests.get(url, params=params, timeout=30).json()
    user_groups_set = set(response['response']['items'])
    return(user_groups_set)

def get_user_friends():
    user_id = find_user_id(user)
    params = {
        'access_token': token,
        'v': 5.92,
        'user_ids': user_id
        }
    url = 'https://api.vk.com/method/friends.get' 
    response = requests.get(url, params=params, timeout=30).json()
    friends_list_id = response['response']['items']
    return(friends_list_id)
    

def get_friends_group():
    friends_list_id = get_user_friends()
    friends_group = []
    count = 1
    for friend in friends_list_id:
        url = 'https://api.vk.com/method/groups.get'
        params = {
                'access_token': token,
                'v': 5.92,
                'user_id': friend
                }
        response = requests.get(url, params=params, timeout=30).json()
        if 'error' in response:
            continue
        else:
            friends_group.extend(response['response']['items'])
        print('Проверены группа друга № {}'.format(count))
        time.sleep(3)
        count += 1
    friends_group_set = set(friends_group)
    return(friends_group_set)


def get_group_list():
    user_groups_set = get_user_groups()
    friends_group_set = get_friends_group()
    only_user_groups = user_groups_set.difference(friends_group_set)
    group_list = []
    for group in only_user_groups:
        group_info_dict ={}
        params = {
                'access_token': token,
                'v': 5.92,
                'group_id': group,
                'fields': 'members_count'
                }
        url = 'https://api.vk.com/method/groups.getById'
        response = requests.get(url, params=params, timeout=30).json()
        group_info_dict['name'] = (response['response'][0]['name'])
        group_info_dict['gid'] = (response['response'][0]['id'])
        group_info_dict['members_count'] = (response['response'][0]['members_count'])
        group_list.append(group_info_dict)
    return(group_list)


def write_group_list_json():
    group_list = get_group_list()
    with open ('groups.json', 'w') as f:
        f.write(json.dumps(group_list))
    

if __name__ == '__main__':
    write_group_list_json()
pass
    
