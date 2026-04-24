import logging
import subprocess
import csv
import numpy as np
import pandas as pd
from tabulate import tabulate

logger = logging.getLogger('driverquery')

class DriverQuery:
    def __init__(self, filename='drivers.csv', driver_type='File System '):
        self.filename = filename
        self.driver_type = driver_type
        drivers = self.get_data()
        self.save_data(drivers)
        self.data = self.load_data()

    @staticmethod
    def get_data():
        try:
            result = subprocess.run(['driverquery', '/V', '/FO', 'CSV'],
                                    stdout=subprocess.PIPE)
            data = result.stdout.decode('utf-8')
            return data
        except Exception:
            logger.error("Unable to fetch the driverquery data")
            raise

    def save_data(self, text_data):
        with open(self.filename, 'w', encoding='utf-8') as output:
            output.write(str(text_data))

    def load_data(self):
        return pd.read_csv(self.filename, encoding='utf-8')

    def __str__(self):
        df = self.load_data()
        # fill nan with empty str
        df = df.fillna('')
        subset = df[['Module Name', 'Display Name', 'Driver Type', 'Link Date']]
        filtered = subset[subset['Driver Type'] == self.driver_type]
        # On Windows replace method for NaN doesn't work properly for columns with non-numeric values
        return str(tabulate(filtered.replace(np.nan, None), headers='keys', showindex=False))


if __name__ == '__main__':
    drivers = DriverQuery()
    print(drivers)

