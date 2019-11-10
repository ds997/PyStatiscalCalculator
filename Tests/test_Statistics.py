import unittest
from CsvReader.CsvReader import CsvReader
from Statistics.Statistics import Statistics


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.Statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.Statistics, Statistics)

    def test_mean(self):
        test_data = CsvReader('Tests/Data/population_list.csv').data
        test_result = CsvReader('Tests/Data/result_data.csv').data
        result_test = 0
        for column in test_result:
            result_test = float(column['Mean'])

        list1 = []
        for row in test_data:
            result = float(row['List1'])
            list1.append(result)

        self.Statistics.mean(list1)
        self.assertEqual(round(self.Statistics.result), round(result_test))

    def test_median(self):
        test_data = CsvReader('Tests/Data/population_list.csv').data
        test_result = CsvReader('Tests/Data/result_data.csv').data

        for column in test_result:
            result_test = float(column['Median'])

        list1 = []

        for row in test_data:
            result = float(row['List1'])
            list1.append(result)

        self.Statistics.median(list1)
        self.assertEqual(round(self.Statistics.result), round(result_test))

    def test_mode(self):
        test_data = CsvReader('Tests/Data/population_list.csv').data
        test_result = CsvReader('Tests/Data/result_data.csv').data

        for column in test_result:
            result_test = float(column['Mode'])

        list1 = []

        for row in test_data:
            result = float(row['List1'])
            list1.append(result)

        self.Statistics.mode(list1)
        self.assertEqual(round(self.Statistics.result), round(result_test))

    def test_standard_deviation(self):
        test_data = CsvReader('Tests/Data/population_list.csv').data
        test_result = CsvReader('Tests/Data/result_data.csv').data

        for column in test_result:
            result_test = float(column['Standard Deviation'])

        list1 = []

        for row in test_data:
            result = float(row['List1'])
            list1.append(result)

        self.Statistics.standard_deviation(list1)
        self.assertEqual(round(self.Statistics.result), round(result_test))

    def test_variance(self):
        test_data = CsvReader('Tests/Data/population_list.csv').data
        test_result = CsvReader('Tests/Data/result_data.csv').data

        for column in test_result:
            result_test = float(column['Variance'])

        list1 = []

        for row in test_data:
            result = float(row['List1'])
            list1.append(result)

        self.Statistics.variance(list1)
        self.assertEqual(round(self.Statistics.result), round(result_test))

    def test_sample_mean(self):

        test_data = CsvReader('Tests/Data/population_list.csv').data
        test_result = CsvReader('Tests/Data/result_data.csv').data

        for column in test_result:
            result_test = float(column['Sample Mean'])

        list1 = []

        for row in test_data:
            result = float(row['List1'])
            list1.append(result)

        self.assertEqual(round(self.Statistics.sample_mean(list1)), round(result_test))


if __name__ == '__main__':
    unittest.main()
