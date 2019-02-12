# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 16:57:27 2019

@author: Bruno
"""

import unittest
import math
import filecmp
import time

class Testing(unittest.TestCase):
    
    def test_ceil(self):
        self.assertEqual(math.ceil(21.1),22) #Right
        self.assertNotEqual(math.ceil(21.1),21)
        with self.assertRaises(TypeError):   #B
            math.ceil('21.1')
        with self.assertRaises(NameError):   
            math.ceil(test)
        with self.assertRaises(AttributeError):   
            math.cil(test)
    
    def test_factorial(self):
        self.assertEqual(math.factorial(10),3628800)
        self.assertNotEqual(math.factorial(10),3628801)
        with self.assertRaises(ValueError):   #B
            math.factorial(10.1)
        with self.assertRaises(NameError):   #B
            math.factorial(test)
        with self.assertRaises(TypeError):   #B
            math.factorial()
        with self.assertRaises(AttributeError):   #B
            math.factoril() 
    
    def test_pow(self):
        self.assertEqual(math.pow(2,2),4)
        self.assertNotEqual(math.pow(2,2),5)
        self.assertEqual(round(math.pow(2.13,2)),5)
        with self.assertRaises(NameError):   #B
            math.pow(test)
        with self.assertRaises(TypeError):   #B
            math.pow('2.1',2)
        with self.assertRaises(AttributeError):   #B
            math.pwo()        
        
        
    def test_filecmp(self):
        self.assertEqual(filecmp.cmp('fruit1.txt','fruit3.txt'),True) #Right
        self.assertEqual(filecmp.cmp('empty1.txt','empty2.txt'),True)
        self.assertEqual(filecmp.cmp('fruit1.txt','fruit2.txt'),False)
        with self.assertRaises(FileNotFoundError):   #B
            filecmp.cmp('fruit1.txt','fruit4.txt')
            
    def test_timeclock(self):
        t0 = time.clock()
        time.sleep(2)
        print(time.clock())
        resta = time.clock() - t0
        self.assertEqual(round(time.clock() - t0), 2)
        with self.assertRaises(NameError):   #B
            time.clock(test)
        with self.assertRaises(AttributeError):   #B
            time.clk()        

if __name__ == '__main__':
    unittest.main()
    
    