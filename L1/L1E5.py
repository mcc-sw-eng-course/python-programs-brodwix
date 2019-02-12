# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 13:46:12 2019

@author: Bruno
"""

# Program that receives as parameters how many Fibonnaci numbers to 
# generate provided by user

def fibonacci(nterms):
    n1 = 0
    n2 = 1
    count = 0
    
    if nterms <= 0:
        print("Please enter a positive integer")
    elif nterms == 1:
       print("Fibonacci sequence upto",nterms,":")
       print(n1)
    else:
       print("Fibonacci sequence upto",nterms,":")
    while count < nterms:
       print(n1,end=' , ')
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
    

print ("please enter a positive integer")
n = input()
intn = int(n)      
fibonacci(intn)