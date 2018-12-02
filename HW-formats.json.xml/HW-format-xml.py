# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 17:03:49 2018

@author: AS
"""

#прочитать файл
from collections import Counter

import xml.etree.ElementTree as ET
parser = ET.XMLParser(encoding='utf-8')
tree = ET.parse('newsafr.xml', parser=parser)
root = tree.getroot()

#получить все слова из тега description и засунуть в список

xml_items = root.findall('channel/item')

description_list = []

for item in xml_items:
    description = (item.find('description').text.split(' '))
    description_list.extend(description)
    
#записать все слова длиннее 6 слов
words_list = []
    
for i in description_list[:]:
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

