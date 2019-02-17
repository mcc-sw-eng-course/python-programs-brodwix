# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 16:47:57 2019

@author: Bruno
"""
import unittest
import coverage
import csv
import numpy 
import os
from L1E82 import L1E8
from L1E82 import n_percentil

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'dataset2.csv')


class MyTest(unittest.TestCase):

   def test_1(self):
       self.assertIsInstance(L1E8('dataset2.csv'), tuple)
       self.assertNotEqual(L1E8('dataset2.csv'), 0 )
       self.assertEqual(L1E8('dataset2.csv')[0], 1106021.0)
       self.assertNotIsInstance(L1E8('dataset2.csv')[1],list )
       self.assertNotIsInstance(L1E8('dataset2.csv')[1], tuple)
       self.assertNotIsInstance(L1E8('dataset2.csv')[1], bytearray)
       self.assertEqual(round((L1E8('dataset2.csv')[2])), 5317)
       self.assertEqual(round((L1E8('dataset2.csv')[3])), 2763)
       self.assertEqual(round((L1E8('dataset2.csv')[4])), 5700)


   def testb(self):
       self.assertIsInstance(n_percentil('dataset2.csv'), float)



if __name__ == '__main__':
    unittest.main()