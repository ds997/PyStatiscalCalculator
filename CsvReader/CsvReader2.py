import csv
from CsvReader.CsvReader import ClassFactory
from FileUtilities.absolutepath import absolutepath


class CsvReader2:
    data = list()

    try:
        def __init__(self, filepath):
            self.data = list()

            with open(absolutepath(filepath)) as text_data:
                csv_data = csv.reader(text_data, delimiter=',')
                next(csv_data)
                for row in csv_data:
                    self.data.append(float(row[0]))
            pass

    except FileNotFoundError as e:
        print("FileNotFoundError Exception :-->", e)
        assert 0

    def return_data_as_objects(self, class_name):
        objects = list()
        for row in self.data:
            objects.append(ClassFactory(class_name, row))
        return objects
