# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 23:22:25 2018

@author: AS
"""


with open('cook_book.txt') as f:
    cook_book = {}
    for line in f:
        dish = line.strip() #1 строка - название блюда
        qty = f.readline().strip() #количество ингредиентов
        ingredients_list = [] 
        for i in range(int(qty)): #цикл по ингредиентам
            ingredient = f.readline().strip().split(' | ') 
            ingredients_list.append(dict(zip(['ingredients_name', 'qty', 'measure'], ingredient)))
        f.readline() #прочитать разделитель
        cook_book[dish] = ingredients_list


def shop_list(dishes, person = 1):
    shop_dict = {}
    ingr_list = []
    for dish in dishes:
        if dish in cook_book.keys(): #проверить является ли он ключом в словаре cook_book и вернуть значение
            for i in range(len(cook_book[dish])):
                ingr_list.append(cook_book[dish][i])
    key_ingr_list = ['measure', 'quantity']
    for i in range(len(ingr_list)):
        qty_msr = [ingr_list[i]['measure'], int(ingr_list[i]['qty'])*person]
        ingr_name = ingr_list[i]['ingredients_name']
        qty_msr_dict = dict(zip(key_ingr_list, qty_msr))
        ingr_qty_msr_dict = {ingr_name : qty_msr_dict}
        shop_dict.update(ingr_qty_msr_dict)
    print(shop_dict)
            
shop_list(['Омлет', 'Запеченный картофель'], 5)
