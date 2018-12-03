# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 18:48:12 2018

@author: AS
"""

#Необходимо реализовать менеджер контекста, печатающий на экран:
#
#Время запуска кода в менеджере контекста;
#Время окончания работы кода;
#Сколько было потрачено времени на выполнение кода.


import datetime

from contextlib import contextmanager

@contextmanager

def run_time():
    try:
        start_time = (datetime.datetime.now())
        print(start_time)
        yield
    finally:
        end_time = (datetime.datetime.now())
        print(end_time)
        print('Время на выполнение кода: {}'.format(end_time - start_time))


animals_list = [
  {'name': 'Grey', 'weight': 3, 'voice': 'ga-ga-ga', 'eggs': 0, 'animal_type': 'goose', 'hungry': False}, 
  {'name': 'White', 'weight': 4, 'voice': 'ga-ga-ga', 'eggs': 0, 'animal_type': 'goose', 'hungry': False}, {'name': 'Manya', 'weight': 151, 'voice': 'mooooo', 'milk': 0.5, 'animal_type': 'cow', 'hungry': False}, {'name': 'Barashek', 'weight': 41, 'voice': 'beeeee', 'wool': 0.5, 'animal_type': 'sheep', 'hungry': False}, {'name': 'Kudryaviy', 'weight': 46, 'voice': 'beeeee', 'wool': 0.5, 'animal_type': 'sheep', 'hungry': False}, {'name': 'Koko', 'weight': 3, 'voice': 'ko-ko-ko', 'eggs': 1, 'animal_type': 'chicken', 'hungry': False}, 
  {'name': 'Kukareku', 'weight': 2, 'voice': 'ko-ko-ko', 'eggs': 1, 'animal_type': 'chicken', 'hungry': False}, {'name': 'Horn', 'weight': 16, 'voice': 'meeeee', 'milk': 0.0, 'animal_type': 'goat', 'hungry': False}, 
  {'name': 'Hoove', 'weight': 18, 'voice': 'meeeee', 'milk': 0.0, 'animal_type': 'goat', 'hungry': False}, 
  {'name': 'Kryakva', 'weight': 3, 'voice': 'krya-krya-krya', 'eggs': 0, 'animal_type': 'duck', 'hungry': False}
  ]    

with run_time():
    animals_list.sort(key=lambda k: k['weight'])
    print(animals_list[-1]['name'])