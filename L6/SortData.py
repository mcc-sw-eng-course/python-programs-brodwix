from pathlib import Path
import os
import csv


class Sorter:
    def __init__(self):
        self.readfile = ""
        self.writefile = ""

    def set_input_data(self, file_location):
        file = Path(file_location)
        if not file.is_file():
            raise ValueError("file not found")
        try:
            data = []
            with open(file_location, 'r') as f:
                reader = csv.reader(f, delimiter=',')
                for row in f:
                    result = data.append(int(row[4].replace(',', '')))

                self.readfile = result

        except:
            raise ValueError("could not open file")
        return self.readfile

    def set_output_data(self, file_location ):
        file = Path(file_location )
        if file.is_file():
            raise ValueError("file already exists")
        try:
            with open(file_location, 'x') as f:
                writer = csv.writer(f)
                self.writefile = list(writer)

        except:
            raise ValueError("could not create file")
        return self.writefile

    def mergeSort(self,list):
        if len(list) > 1:
            mid = len(list) // 2  # Finding the mid of the array
            L = list[:mid]  # Dividing the array elements
            R = list[mid:]  # into 2 halves

            self.mergeSort(L)  # Sorting the first half
            self.mergeSort(R)  # Sorting the second half

            i = j = k = 0

            # Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    list[k] = L[i]
                    i += 1
                else:
                    list[k] = R[j]
                    j += 1
                k += 1

            # Checking if any element was left
            while i < len(L):
                list[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                list[k] = R[j]
                j += 1
                k += 1


