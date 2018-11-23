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


def shop_list(dishes, person = 1):
    shop_dict = {}
    ingr_list = []
    for dish in dishes:
        if dish in cook_book.keys(): #проверить является ли он ключом в словаре cook_book и вернуть значение
            for i in range(len(cook_book[dish])):
                ingr_list.append(cook_book[dish][i])
            pass
    key_ingr_list = ['measure', 'quantity']
    for i in range(len(ingr_list)):
        qty_msr = [ingr_list[i]['measure'], int(ingr_list[i]['qty'])*person]
        ingr_name = ingr_list[i]['ingredients_name']
        temp_dict = dict(zip(key_ingr_list, qty_msr))
        temp_dict2 = {ingr_name : temp_dict}
        shop_dict.update(temp_dict2)
        pass
    pass
    print(shop_dict)
            
shop_list(['Омлет', 'Запеченный картофель'], 5)
