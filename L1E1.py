# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 16:52:12 2019

@author: Bruno
"""
num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")