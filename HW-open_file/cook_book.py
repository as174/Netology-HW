# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 23:22:25 2018

@author: RU20009341
"""

keys_list = ['ingredients_name', 'qty', 'measure']
cook_book = {}

with open('cook_book.txt') as f:
    for line in f:
        dish = line.strip() #1 строка - название блюда
        qty = f.readline().strip() #количество ингредиентов
        ingredients_list = [] 
        for i in range(int(qty)): #цикл по ингредиентам
            ingredient = f.readline().strip().split(' | ') 
            ingredients_list.append(dict(zip(keys_list, ingredient)))
        pass
        f.readline() #прочитать разделитель
        cook_book[dish] = ingredients_list
    pass
pass 

for k in cook_book.keys():
    print(k, '\n', cook_book[k], '\n')
pass


#            ingredients_dict = {}
#            ingredients_dict['ingredients_name'] = kuku[0].strip()
#            ingredients_dict['qty'] = kuku[1].strip()
#            ingredients_dict['measure'] = kuku[2].strip()
                