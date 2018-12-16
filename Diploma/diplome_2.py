# -*- coding: utf-8 -*-
"""

@author: AS
"""

#Вывести список групп в ВК в которых состоит пользователь, 
#но не состоит никто из его друзей.

#1. найти все группы, в которых состоит юзер. Записать в множество user_groups_set
#2. найти всех друзей юзера. Записать их в список friends_list
#3. найти все группы друзей юзера, записать во множество friends_group_set
#4. найти группы из первого множества, которых нет во втором set.symmetric_difference(other); 
#встречающихся в одном множестве, но не встречающиеся в обоих. Запишем в only_user_groups
#5. для групп из последнего множества находим {
#    “name”: “Название группы”, 
#    “gid”: “идентификатор группы”, 
#    “members_count”: количество_участников_сообщества
#    },

import requests
import time

token  = 'ed1271af9e8883f7a7c2cefbfddfcbc61563029666c487b2f71a5227cce0d1b533c4af4c5b888633c06ae'

#user_name = 'eshmargunov'

#user_id = '171691064'

#user_id = input('Введите id пользователя:')

#1. найти все группы, в которых состоит юзер. Записать в множество user_groups_set
#def get_user_groups(user_id):
#    params = {
#        'access_token': token,
#        'v': 5.92,
#        'user_ids': user_id
#        }
#    url = 'https://api.vk.com/method/groups.get' 
#    response = requests.get(url, params=params, timeout=30).json()
#    user_groups_set = set(response['response']['items'])
#    return(user_groups_set)

#2. найти всех друзей юзера. Записать их в список friends_list
#def get_user_friends(user_id):
#    params = {
#        'access_token': token,
#        'v': 5.92,
#        'user_ids': user_id
#        }
#    url = 'https://api.vk.com/method/friends.get' 
#    response = requests.get(url, params=params, timeout=30).json()
#    friends_list_id = response['response']['items']
#    return(friends_list_id)

#friends_list_id = get_user_friends(user_id)


#3. найти все группы друзей юзера, записать во множество friends_group_set

#попробуем на примере 2 друзей в списке
friends_list_id = [4929, 7858]

friends_group = []
count = 1
for friend in friends_list_id:
    url = 'https://api.vk.com/method/groups.get'
    params = {
        'access_token': token,
        'v': 5.92,
        'user_ids': friend
        }
    response = requests.get(url, params=params, timeout=30).json()
    print(response)
    friends_group.append(response['response']['items'])
    print('Выполнена итерация номер {}'.format(count))
    time.sleep(3)
    count += 1
    
print(friends_group)








