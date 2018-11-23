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

#создаем пустой словарь shop_list
#передаем в функцию параметры - ключи и количество персон
#получаем название блюда - ключ
#берем значение ключа - список
#делаем цикл по списку
#в списке находим ingredients_name и его значение используем в качестве ключа для shop_list



#shop_list = {}
#msr_qty_list = []
#
#a = cook_book['Омлет'][0]['ingredients_name'] 
#msr = cook_book['Омлет'][0]['measure'] 
#qty = cook_book['Омлет'][0]['qty'] 
#shop_list[a] = msr_qty



#def shop_list(dishes):
#    ingr_list = []
#    for dish in dishes:
#        if dish in cook_book.keys(): #проверить является ли он ключом в словаре cook_book и вернуть значение
#            print(cook_book[dish], '\n')
#        pass
#    pass

def shop_list(dishes):
    shop_dict = {}
    ingr_list = []
    for dish in dishes:
        if dish in cook_book.keys(): #проверить является ли он ключом в словаре cook_book и вернуть значение
            for i in range(len(cook_book[dish])):
                ingr_list.append(cook_book[dish][i])
            pass
    print(ingr_list)
    key_ingr_list = ['measure', 'quantity']
    for i in range(len(ingr_list)):
        for k in i:
            qty_msr = [ingr_list['measure'], ingr_list['qty']]
            ingr_name = ingr_list['ingredients_name']
            temp_dict = dict(zip(key_ingr_list, qty_msr))
            temp_dict2 = {ingr_name : temp_dict}
            shop_dict.append(temp_dict2)
        pass
    pass
    print(shop_dict)
            
shop_list(['Омлет', 'Запеченный картофель'])

#пройти итератором по списку словарей, взять значение ключа "ingredients name", 
#сложить значение ключа "qty" и вывести значение из "measure"
            

#
#def shop_list(*args):
#    for k in cook_book.keys():
#        if 

#def get_shop_list_by_dishes(dishes):
#    shop_list = {}
#    for dishes in cook_book.keys():
#        shop_list = (cook_book[dishes]).append
#        print(shop_list.values())
#    pass
#
#get_shop_list_by_dishes(['Омлет', 'Фахитос'])

#shop_list = {}
#
#for v in cook_book.values():
    
    

#Нужно написать функцию, которая на вход принимает список блюд из cook_book и количество персон
#get_shop_list_by_dishes(dishes, person_count)
#На выходе мы должны получить словарь с названием ингредиентов и его количетсва для блюда. 
#get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
#Должен быть следующий результат:
#
#{
#  'Картофель': {'measure': 'кг', 'quantity': 2},
#  'Молоко': {'measure': 'мл', 'quantity': 200},
#  'Помидор': {'measure': 'шт', 'quantity': 8},
#  'Сыр гауда': {'measure': 'г', 'quantity': 200},
#  'Яйцо': {'measure': 'шт', 'quantity': 4},
#  'Чеснок': {'measure': 'зубч', 'quantity': 6}
#}
