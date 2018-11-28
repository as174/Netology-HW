# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 20:34:39 2018

@author: AS
"""
# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C
 # Пример на настоящих данных
 # python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1
 # не забываем организовывать собственный код в функции
 
 
import os

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))

os.path.join(current_dir, migrations) #путь до папки Migrations
file_list = (os.listdir(os.path.join(current_dir, migrations))) #получить список всех файлов в папке Migrations
    
#нужно найти все файлы, которые заканчиваются на .sql и засунуть в список
sql_list = []
   
for file in file_list:
    if '.sql' in file:
        sql_list.append(file)

#Нужно написать функцию на чтение файла
    
def read_file(file_name, encoding='utf-8'):
    with open(file_name) as f:
        info = f.read()
        info = str.lower(info)
        return(info)
         
#Сделаем функцию, которая запрашивает инпут и выводит список файлов, а также их количество

#def sql_file_search(sql_list):
#    word = input('Введите строку:')
#    word = str.lower(word)
#    file_found = []
#    for sql_file in sql_list:
#        sql_file_path = (os.path.join(current_dir, migrations, sql_file))
#        opened_file = read_file(sql_file_path)
#        if word in opened_file:
#            file_found.append(os.path.join(migrations, sql_file))
#        print(*file_found, '\n')
#        print('Всего: ', len(file_found))
#    
#Изменим так, чтобы функция работала пока не останется 1 файл
        
def sql_file_search(sql_list):
    file_list = sql_list
    while True:
        word = input('Введите строку: ')
        word = str.lower(word)
        result_list = []
        for file in file_list:
            file_path = (os.path.join(current_dir, migrations, file))
            opened_file = read_file(file_path)
            if word in opened_file:
                result_list.append(file)
        print(*result_list, '\n')
        print('Всего: ', len(result_list))    
        file_list = result_list



  
if __name__ == '__main__':   

    sql_file_search(sql_list)
           
pass 