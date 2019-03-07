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

    def test_qSort(self):
        self.list.append(5)
        self.list.append(7)
        self.list.append(3)
        self.list.append(56)
        self.list.append(2)
        self.list.append(5)
        self.list.append(7)
        self.list.append(63)
        ordered = Sorter.mergeSort(self.list)
        self.assertEqual(ordered, ([2, 3, 5, 5, 7, 7, 56, 63]))