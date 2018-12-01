# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 01:19:30 2018

@author: AS
"""
#Написать программу, 
#которая будет выводить топ 10 самых часто встречающихся в новостях слов
# длиннее 6 символов для каждого файла.



#записать все слова длиннее 6 слов

import json
from collections import Counter

#прочитать файл
#получить данные из description
with open('newsafr.json', encoding = 'utf-8') as datafile:
    json_data = json.load(datafile)
    for data in json_data.values():
        news_dict = (data['channel'])
        

#взять все слова и засунуть в один список
for items in news_dict.items():
    news_list = (news_dict['items'])

news_l = []

for news in news_list:
    news_l.extend((news['description'].split(' ')))
    
#записать все слова длиннее 6 слов
words_list = []
    
for i in news_l[:]:
    if len(i) > 6:
        words_list.append(i)

#записать в словарь, где каждое слово - ключ, а каждое значение - количество упоминаний этого слова
words_counter = Counter(words_list)

#т.к. словарь содержит неупорядоченные значения, то переделываем в кортежи
words_list = list(words_counter.items())
    
#сортируем по второму элементу кортежа
words_list.sort(key=lambda x: x[1])

#берем топ 10 встречающихся слов
top_list = words_list[:-11:-1]
top_words = []
for tuple in top_list:
    top_words.append(tuple[0])
print('Топ 10 самых встречающихся слов длиннее 6 букв: ', '\n', top_words)

