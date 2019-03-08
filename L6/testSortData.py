from SortData import Sorter
import unittest
import random
from pathlib import Path
import math
import os

class FileSort_test(unittest.TestCase):
    def setUp(self):
        self.list = []
        self.FileSorter = Sorter()
        self.file = "test.data"
        self.elements = 100000

        file = Path(self.file)
        if file.is_file():
            os.remove(self.file)

    def test_mergeSort(self):
        self.list.append(5)
        self.list.append(7)
        self.list.append(3)
        self.list.append(56)
        self.list.append(2)
        self.list.append(5)
        self.list.append(7)
        self.list.append(63)
        a = self.list
        ordered = self.FileSorter.mergeSort(a)
        self.assertEqual(ordered, ([2, 3, 5, 5, 7, 7, 56, 63]))

    def test_heapSort(self):
        self.list.append(5)
        self.list.append(7)
        self.list.append(3)
        self.list.append(56)
        self.list.append(2)
        self.list.append(5)
        self.list.append(7)
        self.list.append(63)
        self.assertEqual(self.FileSorter.heapSort(self.list),[2,3,5,5,7,7,56,63])

    def test_qSort(self):
        self.list.append(5)
        self.list.append(7)
        self.list.append(3)
        self.list.append(56)
        self.list.append(2)
        self.list.append(5)
        self.list.append(7)
        self.list.append(63)
        self.assertEqual(self.FileSorter.quickSort((self.list),0,7),[2,3,5,5,7,7,56,63])

    def test_set_input_data_exception(self):
        with self.assertRaises(ValueError):
            self.FileSorter.set_input_data("awddq")

    def test_set_input_data_success(self):
        file=open(self.file,"x")
        self.FileSorter.set_input_data(self.file)
        self.assertEqual(self.FileSorter.readfile,self.list)
        file.close()
        os.remove(self.file)


    def test_set_input_data_with_invalid_paths(self):
        with self.assertRaises(TypeError):
            self.FileSorter.set_input_data(48)
        with self.assertRaises(ValueError):
            self.FileSorter.set_input_data("test0.csv")


    def test_set_input_data_with_valid_paths(self):
        self.assertTrue(self.FileSorter.set_input_data("inputlist.csv"))
        self.assertIsNotNone(self.FileSorter.readfile)
        self.assertIsInstance(self.FileSorter.readfile, list)
        self.assertEqual(100, len(self.FileSorter.readfile[0]))


