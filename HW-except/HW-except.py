# -*- coding: utf-8 -*-
polskaya_notacia = input('Введите аргументы польской нотации: ')
arguments_list = polskaya_notacia.split()

arguments_list[1] = int(arguments_list[1])
arguments_list[2] = int(arguments_list[2])

assert arguments_list[1] >= 0 
assert arguments_list[2] >= 0

if arguments_list[0] == '+':
    print(arguments_list[1] + arguments_list[2])
elif arguments_list[0] == '-':
    print(arguments_list[1] - arguments_list[2])
elif arguments_list[0] == '*':
    print(arguments_list[1] * arguments_list[2])
elif arguments_list[0] == '/':
    try:
        print(arguments_list[1] / arguments_list[2])
    except ZeroDivisionError: 
        print('На ноль делить нельзя')
else:
    print('Оператор не найден. Попробуйте еще раз')
