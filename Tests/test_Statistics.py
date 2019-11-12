import unittest
from CsvReader.CsvReader import CsvReader
from CsvReader.CsvReader2 import CsvReader2
from Statistics.Statistics import Statistics


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.Statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.Statistics, Statistics)

    def test_mean(self):
        test_data = CsvReader('Tests/Data/population_list.csv').data
        result_data = CsvReader('Tests/Data/result_data.csv').data

        for column in result_data:
            mean_value = float(column['Mean'])

        data = []

        for row in test_data:
            result = float(row['List1'])
            data.append(result)

        self.Statistics.mean(data)
        self.assertEqual(round(self.Statistics.result), round(mean_value))

    def test_median(self):
        test_data = CsvReader('Tests/Data/population_list.csv').data
        result_data = CsvReader('Tests/Data/result_data.csv').data

        for column in result_data:
            median_value = float(column['Median'])

        data = []

        for row in test_data:
            result = float(row['List1'])
            data.append(result)

        self.Statistics.median(data)
        self.assertEqual(round(self.Statistics.result), round(median_value))

    def test_mode(self):
        test_data = CsvReader('Tests/Data/population_list.csv').data
        result_data = CsvReader('Tests/Data/result_data.csv').data

        for column in result_data:
            mode_value = float(column['Mode'])

        data = []

        for row in test_data:
            result = float(row['List1'])
            data.append(result)

        self.Statistics.mode(data)
        self.assertEqual(round(self.Statistics.result), round(mode_value))

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

    def test_standardized_score(self):

        test_data = CsvReader2('Tests/Data/population_list.csv').data
        test_result = CsvReader2('Tests/Data/result_zscore.csv').data
        '''
        for column in test_result:
            result_test = float(column['Z_score'])
        
        list1 = list()

        for row in test_data:
            result = float(row[0])
            list1.append(result)
        '''
        self.assertListEqual(self.Statistics.z_score(test_data), test_result)

    def test_z_score(self):

            test_data = CsvReader2('Tests/Data/population_list.csv').data
            test_result = CsvReader2('Tests/Data/result_zscore.csv').data
            '''
            for column in test_result:
                result_test = float(column['Z_score'])
            
            list1 = list()

            for row in test_data:
                result = float(row[0])
                list1.append(result)
            '''
            self.assertListEqual(self.Statistics.z_score(test_data), test_result)


    def test_pop_correlation_coefficient(self):

            test_data = CsvReader2('Tests/Data/population_list.csv').data
            test_result = CsvReader('Tests/Data/result_data.csv').data

            for column in test_result:
                result_test = float(column['Pop_correlation_coefficient'])
            '''
            list1 = []

            for row in test_data:
                result = float(row['List1'])
                list1.append(result)
            '''
            self.assertEqual(round(self.Statistics.pop_correlation_coefficient(test_data)), round(result_test))

    def test_sample_standard_deviation(self):

        test_data = CsvReader('Tests/Data/population_list.csv').data
        test_result = CsvReader('Tests/Data/result_data.csv').data

        for column in test_result:
            result_test = float(column['Sample_Standard_Deviation'])

        list1 = []

        for row in test_data:
            result = float(row['List1'])
            list1.append(result)

        self.assertEqual(round(self.Statistics.sample_standard_deviation(list1)), round(result_test))

    def test_proportion_calculator(self):
        test_data = CsvReader('Tests/Data/population_list.csv').data
        test_result = CsvReader('Tests/Data/result_data.csv').data

        list1 = []

        for column in test_result:
            result_test = float((column['Proportion_result']))

        for row in test_data:
            result= float(row['List1'])
            list1.append(result)

        self.assertEqual(round(self.Statistics.proportion(list1)),round(result_test))

    def test_sample_variance_calculator(self):
        print(' ')
        print('Testing Population Variance')
        test_data = CsvReader('Tests/Data/population_list.csv').data
        test_result = CsvReader('Tests/Data/result_data.csv').data

        list1  = []

        for column in test_result:
            result_test = float((column['Variance_Sample_result']))

        for row in test_data:
            result = int(row['List1'])
            list1.append(result)

        self.assertEqual(round(self.Statistics.sample_variance(list1)),round(result_test))



if __name__ == '__main__':
    unittest.main()
