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

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'dataset2.csv')


class MyTest(unittest.TestCase):

   def setUp(self):
       self.testdata = open(TESTDATA_FILENAME).read()