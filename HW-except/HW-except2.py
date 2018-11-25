# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 19:00:59 2018

@author: AS
"""

documents = [
   {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
   {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
   {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
   {"type": "INN", "number": "771231230213"},] #для исключения keyerror

directories = {
  '1': ['2207 876234', '11-2'],
  '2': ['10006'],
  '3': []
}

# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;

def people(command):
  doc_number = str(input('Введите номер документа, чтобы узнать имя: '))
  result = 'Документ отсутствует'
  for data in command:
    if doc_number == data['number']:
      result = (data['name'])
      break
  print(result)


# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";

def documents_list(command):
  for data in command:
    data_list = [data['type'], data['number'], data['name']]
    print(data_list[0], ' "', data_list[1], '" ', data_list[2], sep='')

# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;

def shelf(command):
  doc_number = str(input('Введите номер документа, чтобы узнать полку: '))
  result = 'Документ отсутствует'
  for key, value in command.items():
    if doc_number in value:
      result = key
    break
  print(result)

# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.

def add(command):
  documents_keys = ['type', 'number', 'name']
  doc_type = str(input('Введите тип документа'))
  doc_number = str(input('Введите номер документа'))
  person_name = str(input('Введите имя человека'))
  shelf_number = str(input('Введите номер полки'))
  documents_values = [doc_type, doc_number, person_name]
  new_doc = dict(zip(documents_keys, documents_values))
  for key, value in command.items():
    if shelf_number in key:
      documents.append(new_doc)
      value.append(doc_number)
  if shelf_number not in directories.keys():
      print('Полка не существует')
      
      
#новой функцией, выводящей имена всех владельцев документов. 
#С помощью исключения KeyError проверяйте, если поле "name" и документа.      

def name(command):
    for data in command:
        try:
            print(data['name'])
        except KeyError:
            print('В документе {} номер {} нет имени владельца'.format(data['type'], data['number']))


command = input('Доступные команды: p, l, s, a, n. \n p – имя человека по номеру документа.\n l - список всех документов. \n s – номер полки по номеру документа. \n a – добавление нового документа в каталог и в перечень полок по номеру, типу, имени владельца и номеру полки, на котором он будет храниться.\n n – имена всех людей, владельцев документов. \n\n Введите команду: ')

if command == 'p':
  people(documents)
elif command == 'l':
  documents_list(documents)
elif command == 's':
  shelf(directories)
elif command == 'a':
  add(directories)
elif command == 'n':
    name(documents)
else:
  print('Команда не существует')

#print(documents)
#print('\n')
#print(directories)

