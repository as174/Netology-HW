# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 12:37:28 2018

@author: AS
"""

#parent class
class animals():
    
    hungry = True
    
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    
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
        print(name, "is not hungry.")
    
    
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

cow_manya = animals('Manya', 150)

sheep_barashek = animals('Barashek', 40)
sheep_kudryaviy = animals('Kudryaviy', 45)

chicken_koko = animals('Koko', 2)
chicken_kukareku = animals('Kukareku', 1)

goat_horn = animals('Horn', 15)
goat_hoove = animals('Hoove', 17)

duck_kryakva = animals('Kryakva', 2)

animals.feed(2)


print(goose_grey.__dict__)



#print(goose_grey.eggs)
#
#goose_grey.pick_eggs(2)
#print(goose_grey.eggs)

