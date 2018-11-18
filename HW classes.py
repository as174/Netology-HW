# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 12:37:28 2018

@author: AS
"""

#parent class
class animals():
    
    hungry = True
    animals_list = []
    
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        animals.animals_list.append(self)
    
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
class goose(animals):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = 'ga-ga-ga'
        self.eggs = 5 #qty
        self.animal_type = 'goose'
        
    def pick_eggs(self, value):
        if value > self.eggs:
            print("The ", self.animal_type, " '", self.name, "' ", "don't have so much eggs.", sep='')
        else:
            self.eggs-= value
            print("You've picked", value, "eggs from", self.name)
            

#Manya
class cow(animals):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = 'mooooo'
        self.milk = 1.500 #l
        self.animal_type = 'cow'
        
    def collect_milk(self, value):
        if value > self.milk:
            print("The ", self.animal_type, " '", self.name, "' ", "don't have so much milk.", sep='')
        else:
            self.milk-= value
            print("You've collected", value, "milk from", self.name)

#Barashek and kudryaviy
class sheep(animals):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = 'beeeee'
        self.wool = 1.5 #kg
        self.animal_type = 'sheep'
        
    def shear(self, value):
        if value > self.wool:
            print("The ", self.animal_type, " '", self.name, "' ", "don't have so much wool.", sep='')
        else:
            self.wool-= value
            print("You've sheared", value, "wool from", self.name)

#co-co and kukareku
class chicken(animals):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = 'ko-ko-ko'
        self.eggs = 3 #qty
        self.animal_type = 'chicken'
        
    def pick_eggs(self, value):
        if value > self.eggs:
            print("The ", self.animal_type, " '", self.name, "' ", "don't have so much eggs.", sep='')
        else:
            self.eggs-= value
            print("You've picked", value, "eggs from", self.name)
        
        
#horns and hooves
class goat(animals):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = 'meeeee'
        self.milk = 0.5 #l
        self.animal_type = 'goat'
        
    def collect_milk(self, value):
        if value > self.milk:
            print("The ", self.animal_type, " '", self.name, "' ", "don't have so much milk.", sep='')
        else:
            self.milk-= value
            print("You've collected", value, "milk from", self.name)
        
#kryakva
class duck(animals):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = 'krya-krya-krya'
        self.eggs = 2 #qty
        self.animal_type = 'duck'
        
    def pick_eggs(self, value):
        if value > self.eggs:
            print("The ", self.animal_type, " '", self.name, "' ", "don't have so much eggs.", sep='')
        else:
            self.eggs-= value
            print("You've picked", value, "eggs from", self.name)
        

goose_grey = goose('Grey', 2)
goose_white = goose('White', 3)

cow_manya = cow('Manya', 150)

sheep_barashek = sheep('Barashek', 40)
sheep_kudryaviy = sheep('Kudryaviy', 45)

chicken_koko = chicken('Koko', 2)
chicken_kukareku = chicken('Kukareku', 1)

goat_horn = goat('Horn', 15)
goat_hoove = goat('Hoove', 17)

duck_kryakva = duck('Kryakva', 2)


chicken_koko.feed(2)


#for animals in animals.animals_list:
#    print(animals.__dict__)




#print(goose_grey.eggs)
#
#goose_grey.pick_eggs(2)
#print(goose_grey.eggs)

