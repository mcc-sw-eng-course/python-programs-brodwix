import csv
import os
import re
from datetime import datetime

# Magic strings for the performance data map
NUM_OF_RECORDS = "num_of_records"
TIME_CONSUMED = "time_consumed"
START_TIME = "start_time"
END_TIME = "end_time"
ALGORITHM = "algorithm"

# Algorithm Identifiers
MERGE_SORT = "Merge Sort"


class DataSorter:

    def __init__(self):
        self.data = []
        self.start_time = datetime.now()
        self.end_time = datetime.now()
        self.algorithm_used = ""
        self.file_path_name =file_path_name

    @staticmethod
    def validate_input_list(input_list: list):
        """
        Validates if input_list is not None and is a list of only int or floats, if the validation doesn't pass
        a ValueError will be raised
        :param input_list: a list of values to validate
        :raises: a ValueError if the validation fails
        """
        if list is None or type(input_list) is not list:
            raise ValueError("The input_list was either None or not a list at all!")

        # Check that all elements are either float or int
        if not all([type(x) is int or type(x) is float for x in input_list]):
            raise ValueError("The input_list contains values that are not int nor float!")

    # Exercise 25
    def set_input_data(self, file_path_name: str):


        if type(file_path_name) is not str:
            raise TypeError

        if not (os.path.exists(file_path_name) and os.path.isfile(file_path_name)):
            raise FileNotFoundError

        if not file_path_name.lower().endswith(".csv"):
            raise NotCSVException

        self.data = []
        with open(file_path_name, newline='') as csvfile:
            try:
                dialect = csv.Sniffer().sniff(csvfile.read(1024), [',', '|'])
            except csv.Error:
                raise NotCSVException
            csvfile.seek(0)
            items = csv.reader(csvfile, dialect)
            for row in items:
                for i in row:
                    if i.isdigit():
                        self.data.append(float(i))
                    elif re.match("^\d+?\.\d+?$", i):
                        self.data.append(float(i))
                    else:
                        raise ValueError("The CSV contains non-numeric values")

        return True

    # Exercise 26
    def set_output_data(self, file_path_name: str):
        if not file_path_name.lower().endswith(".csv"):
            file_path_name = file_path_name + ".csv"
        if len(self.data) == 0:
            raise EmptyDataArrayException
        output = []
        for item in self.data:
            output.append(str(item))
        with open(file_path_name, 'w', newline='') as file:
            writer = csv.writer(file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(output)
        return True

    # Exercise 27
    def execute_merge_sort(self):
        # Remember to track the name of the algorithm in self.algorithm_used
        #  and to store the value of datetime.now() in self.start_time and
        #  self.end_time at appropriate times

        # First validate that the data is valid, if no ValueError is raised, we'll continue
        DataSorter.validate_input_list(self.data)

        self.algorithm_used = MERGE_SORT
        self.start_time = datetime.now()

        # If the list is empty or contains one element, just return and track the endtime
        if not self.data or len(self.data) == 1:
            self.end_time = datetime.now()
            return

        self.data = DataSorter._merge_sort(self.data)
        self.end_time = datetime.now()

    @staticmethod
    def _merge_sort(input_list: list) -> list:

        # This will allow us to recursively splice the input_list until there is only one element
        if len(input_list) > 1:

            middle = len(input_list) // 2
            left = input_list[:middle]
            right = input_list[middle:]

            # Divide the lists until they have one element
            left = DataSorter._merge_sort(left)
            right = DataSorter._merge_sort(right)

            # Merge the two lists, we'll need symmetric indexes for each list and a merged list
            merged_list = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    merged_list.append(left[i])
                    i += 1
                else:
                    merged_list.append(right[j])
                    j += 1

            # If the lists were not symmetrical, we need append the remnant elements to the merged_list

            if i < len(left):
                merged_list.extend(left[i:])

            if j < len(right):
                merged_list.extend(right[j:])

            return merged_list

        else:
            # If the list contains one element, it is considered sorted
            return input_list

    # Exercise 30
    def get_performance_date(self) -> dict:
        return {
            NUM_OF_RECORDS: len(self.data),
            TIME_CONSUMED: self.end_time - self.start_time,
            START_TIME: self.start_time,
            END_TIME: self.end_time,
            ALGORITHM: self.algorithm_used
        }


class NotCSVException(Exception):
    pass


class EmptyDataArrayException(Exception):
    pass