# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 01:19:30 2018

@author: AS
"""
#Написать программу, 
#которая будет выводить топ 10 самых часто встречающихся в новостях слов
# длиннее 6 символов для каждого файла.


import json
from collections import Counter

#прочитать файл
#получить данные из description
with open('newsafr.json', encoding = 'utf-8') as datafile:
    json_data = json.load(datafile)
    news_dict = json_data['rss']['channel']
        

#взять все слова и засунуть в один список

news_list = news_dict['items']

news_l = []

for news in news_list:
    news_l.extend((news['description'].split(' ')))
    
#записать все слова длиннее 6 слов
words_list = []
    
for i in news_l[:]:
    if len(i) > 6:
        words_list.append(i)

words_counter = Counter(words_list).most_common(10)


top_words = []
for tuple in words_counter:
    top_words.append(tuple[0])

print('Топ 10 самых встречающихся слов длиннее 6 букв: ')
for word in top_words:
    print(word)



