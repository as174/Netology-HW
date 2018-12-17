# -*- coding: utf-8 -*-
"""

@author: AS
"""

#Вывести список групп в ВК в которых состоит пользователь, 
#но не состоит никто из его друзей.

#1. найти все группы, в которых состоит юзер. Записать в множество user_groups_set
#2. найти всех друзей юзера. Записать их в список friends_list
#3. найти все группы друзей юзера, записать во множество friends_group_set
#4. найти группы из первого множества, которых нет во втором set.difference(other); 
#встречающихся в одном множестве, но не встречающиеся в обоих. Запишем в only_user_groups
#5. для групп из последнего множества находим {
#    “name”: “Название группы”, 
#    “gid”: “идентификатор группы”, 
#    “members_count”: количество_участников_сообщества
#    },

import requests
import time
import json

token  = 'ed1271af9e8883f7a7c2cefbfddfcbc61563029666c487b2f71a5227cce0d1b533c4af4c5b888633c06ae'



#user_name = 'eshmargunov'
#
#user_id = 171691064

user = input('Введите id пользователя или его user_name:')

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

print(user_id)


##1. найти все группы, в которых состоит юзер. Записать в множество user_groups_set
def get_user_groups(user_id):
    params = {
        'access_token': token,
        'v': 5.92,
        'user_ids': user_id
        }
    url = 'https://api.vk.com/method/groups.get' 
    response = requests.get(url, params=params, timeout=30).json()
    user_groups_set = set(response['response']['items'])
    return(user_groups_set)
    
user_groups_set = get_user_groups(user_id)    
##
###2. найти всех друзей юзера. Записать их в список friends_list
def get_user_friends(user_id):
    params = {
        'access_token': token,
        'v': 5.92,
        'user_ids': user_id
        }
    url = 'https://api.vk.com/method/friends.get' 
    response = requests.get(url, params=params, timeout=30).json()
    friends_list_id = response['response']['items']
    return(friends_list_id)

friends_list_id = get_user_friends(user_id)

print('friends_list_id: ', friends_list_id)
#
#
###3. найти все группы друзей юзера, записать во множество friends_group_set
##
###попробуем на примере 4 друзей в списке
###friends_list_id = [4929, 7858, 11952, 48807]
#
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
print('friends_group_set: ', friends_group_set)
#
#
###4. найти группы из первого множества, которых нет во втором
only_user_groups = user_groups_set.difference(friends_group_set)

print('only_user_groups:', only_user_groups)
#
###only_user_groups = {125927592, 8564, 101522128} - результат
##
###5. для групп из последнего множества находим имя, id, кол-во участников

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

print('group_list:', group_list)

with open ('groups.json', 'w') as f:
    f.write(json.dumps(group_list))
    
#    
#
##    
#    
    