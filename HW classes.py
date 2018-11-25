# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 12:37:28 2018

@author: AS
"""

#parent class
class Animal():
    
    hungry = True
    animals_list = []
    
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        Animal.animals_list.append(self)
    
#    def name(self, value):
#        self.name = value
#    
#    def weight(self, value): #kg
#        self.weight = value
#        
#    def voice(self, value):
#        self.voice = value
#    
    def feed(self, value):
        self.hungry = False
        self.weight += value
        print("You have feed", self.name)
    
    
#дочерние классы

#grey and white
class Goose(Animal):
    
    goose_list =[]
    
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = 'ga-ga-ga'
        self.eggs = 5 #qty
        self.animal_type = 'goose'
        Goose.goose_list.append(self)
        
    def pick_eggs(self, value):
        if value > self.eggs:
            print("The ", self.animal_type, " '", self.name, "' ", "don't have so much eggs.", sep='')
        else:
            self.eggs-= value
            print("You've picked", value, "eggs from", self.name)
            

#Manya
class Cow(Animal):
    
    cow_list =[]
    
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = 'mooooo'
        self.milk = 1.500 #l
        self.animal_type = 'cow'
        Cow.cow_list.append(self)
        
    def collect_milk(self, value):
        if value > self.milk:
            print("The ", self.animal_type, " '", self.name, "' ", "don't have so much milk.", sep='')
        else:
            self.milk-= value
            print("You've collected", value, "milk from", self.name)

#Barashek and kudryaviy
class Sheep(Animal):
    
    sheep_list = []
    
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = 'beeeee'
        self.wool = 1.5 #kg
        self.animal_type = 'sheep'
        Sheep.sheep_list.append(self)
        
    def shear(self, value):
        if value > self.wool:
            print("The ", self.animal_type, " '", self.name, "' ", "don't have so much wool.", sep='')
        else:
            self.wool-= value
            print("You've sheared", value, "wool from", self.name)

#co-co and kukareku
class Chicken(Animal):
    
    chicken_list = []
    
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = 'ko-ko-ko'
        self.eggs = 3 #qty
        self.animal_type = 'chicken'
        Chicken.chicken_list.append(self)
        
    def pick_eggs(self, value):
        if value > self.eggs:
            print("The ", self.animal_type, " '", self.name, "' ", "don't have so much eggs.", sep='')
        else:
            self.eggs-= value
            print("You've picked", value, "eggs from", self.name)
        
        
#horns and hooves
class Goat(Animal):
    
    goat_list = []
    
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = 'meeeee'
        self.milk = 0.5 #l
        self.animal_type = 'goat'
        Goat.goat_list.append(self)
        
    def collect_milk(self, value):
        if value > self.milk:
            print("The ", self.animal_type, " '", self.name, "' ", "don't have so much milk.", sep='')
        else:
            self.milk-= value
            print("You've collected", value, "milk from", self.name)
        
#kryakva
class Duck(Animal):
    
    duck_list = []
    
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = 'krya-krya-krya'
        self.eggs = 2 #qty
        self.animal_type = 'duck'
        Duck.duck_list.append(self)
        
    def pick_eggs(self, value):
        if value > self.eggs:
            print("The ", self.animal_type, " '", self.name, "' ", "don't have so much eggs.", sep='')
        else:
            self.eggs-= value
            print("You've picked", value, "eggs from", self.name)
        

goose_grey = Goose('Grey', 2)
goose_white = Goose('White', 3)

cow_manya = Cow('Manya', 150)

sheep_barashek = Sheep('Barashek', 40)
sheep_kudryaviy = Sheep('Kudryaviy', 45)

chicken_koko = Chicken('Koko', 2)
chicken_kukareku = Chicken('Kukareku', 1)

goat_horn = Goat('Horn', 15)
goat_hoove = Goat('Hoove', 17)

duck_kryakva = Duck('Kryakva', 2)


#chicken_koko.feed(2)
#animals.feed(2)

for Animal in Animal.animals_list:
    Animal.feed(1)

print('\n')

for Goose in Goose.goose_list:
    Goose.pick_eggs(5)
    
for Cow in Cow.cow_list:
    Cow.collect_milk(1)

for Sheep in Sheep.sheep_list:
    Sheep.shear(1)
    
for Chicken in Chicken.chicken_list:
    Chicken.pick_eggs(2)
    
for Goat in Goat.goat_list:
    Goat.collect_milk(0.5)

for Duck in Duck.duck_list:
    Duck.pick_eggs(2)
    
print('\n')

weight = 0

for Animal in Animal.animals_list:
    weight += Animal.weight
print('Вес всех животных: ', weight, 'кг')

all_animals = [goose_grey.__dict__, goose_white.__dict__, cow_manya.__dict__, sheep_barashek.__dict__, sheep_kudryaviy.__dict__, chicken_koko.__dict__, chicken_kukareku.__dict__, goat_horn.__dict__, goat_hoove.__dict__, duck_kryakva.__dict__]

all_animals.sort(key=lambda k: k['weight'])
print('Самое тяжелое животное зовут:', all_animals[-1]['name'])