import unittest
from CsvReader.CsvReader import CsvReader


class MyCsvReaderTest(unittest.TestCase):

    def setUp(self) -> None:
        self.csv_reader = CsvReader('Tests/Data/population_list.csv')

    def test_csv_file(self):
        test_data = CsvReader('Tests/Data/population_list.csv').data
        population_list = []
        item = 0
        for row in test_data:
            item = item + 1
            records = int(row['List1'])
            population_list.append(records)
        self.assertEqual(item, 397)


if __name__ == '__main__':
    unittest.main()
