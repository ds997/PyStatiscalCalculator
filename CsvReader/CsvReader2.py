import csv
from FileUtilities.absolutepath import absolutepath

'''
def ClassFactory(class_name, dictionary):
    return type(class_name, (object,), dictionary)
'''

class CsvReader2:
    data = list()

    def __init__(self, filepath):
        self.data = list()

        with open(absolutepath(filepath)) as text_data:
            csv_data = csv.reader(text_data, delimiter=',')
            next(csv_data)
            for row in csv_data:
                self.data.append(float(row[0]))
        pass

    def return_data_as_objects(self, class_name):
        objects = list()
        for row in self.data:
            objects.append(ClassFactory(class_name, row))
        return objects
