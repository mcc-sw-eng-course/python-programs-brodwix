# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 23:10:46 2019

@author: Bruno
"""

class MyPowerList:

    def __init__(self, name):
        self.name = name
        self.items = []    # creates a new empty list for each dog
        
    def add_item(self, item):
        self.items.append(item)
        
    def remove_item(self, item):
        self.items.remove(item)
    
    def readFromTextFile(self, filename):
        self.filename = filename
        with open(filename) as f:
            lista = f.read().splitlines()
            print(lista)


#Example
         
d = MyPowerList('user1')
e = MyPowerList('user2')

#add new item 
d.items.append('item1')
d.items.append('item2')
d.items.append('item3')

#output ['item1', 'item2', 'item3']

e.items.append('item4')
e.items.append('item5')
e.items.append('item6')

# output ['item4', 'item5', 'item6']

#remove nth item
d.remove_item('item2')
#output: ['item1', 'item3']

#Read from textfile

#e.readFromTextFile("list.txt") ------------- uncomment to read from list.txt

#show item list, input these in python terminal
d.items
e.items

#
