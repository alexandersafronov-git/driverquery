import logging
import subprocess
import numpy as np
import pandas as pd
from tabulate import tabulate
import argparse
import csv

logger = logging.getLogger('driverquery')


class DriverQuery:
    """Runs "driverquery" utility and save the results to a file,
       and then open this file and output only drivers with
       requested driver type ("File System " by default)."""

    def __init__(self, filename='drivers.csv', driver_type='File System ', format_output='TABLE'):
        """ Gets data from "driverquery" and save/load into csv file.

        Args:
            filename: csv file name, optional.
            driver_type:  requested driver type for printing, optional "File System " by default.
            format_output: output format "TABLE" (default) or "CSV"
        """
        self.filename = filename
        self.driver_type = driver_type
        self.format_output = format_output
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
        if self.format_output == 'TABLE':
            # On Windows replace method for NaN doesn't work properly for columns with non-numeric values
            return str(tabulate(filtered.replace(np.nan, None), headers='keys', showindex=False))
        elif self.format_output == 'CSV':
            return filtered.to_csv(index=False, quoting=csv.QUOTE_ALL)
        else:
            raise ValueError('unknown format output: {:s}'.format(self.format_output))


if __name__ == '__main__':
    example_text = '''Usage example:
    driverquery.py --driver_type="Kernel " --fo CSV
    '''
    parser = argparse.ArgumentParser(description='driverquery', epilog=example_text)
    parser.add_argument('-d', '--driver_type', type=str, help='prints only drivers with certain driver type, '
                                                              'default "Files System "', default='File System ')
    parser.add_argument('-f', '--fo', type=str, help='output format: TABLE (by default) or CSV', default='TABLE')
    args = parser.parse_args()
    drivers = DriverQuery(driver_type=args.driver_type, format_output=args.fo)
    print(drivers)
