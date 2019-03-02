from pathlib import Path
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
            with open(file_location, newline='') as f:
                reader = csv.reader(f, delimiter=',',lineterminator='\n', quoting=csv.QUOTE_NONNUMERIC)
                self.readfile = list(reader)
                for row in reader:
                    print(', '.join(row))


        except:
            raise ValueError("could not open file")
        return self.readfile



    def set_output_data(self, file_location):
                      
            with open(file_location, 'x') as f:
                writer = csv.writer(f, quoting = csv.QUOTE_ALL)
                self.writefile = writer.writerow(self.readfile)


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


# Para iniciar el programa, se debe ejecutar
#
# r1 = Sorter()                             ---la clase Sorter se guardará en la variable r1
# a = r1.set_input_data("inputlist.csv")    --- se extraerán los datos de la lista csv y se guardaran en la variable a
# r1.mergeSort(a[0])                        --- se ordenarán los números de menor a mayor usando mergeSort
# r1.set_output_data("out.csv")             --- se guardarán los resultados en un nuevo archivo que se llamará "out.csv"