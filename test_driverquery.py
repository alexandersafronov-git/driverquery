from unittest.mock import patch
from unittest.mock import Mock
from driverquery import DriverQuery

expected_output_table = """Module Name    Display Name    Driver Type    Link Date
-------------  --------------  -------------  -----------
AppvStrm       AppvStrm        File System"""

expected_output_csv = """"Module Name","Display Name","Driver Type","Link Date"
"AppvStrm","AppvStrm","File System ",""
"""
def get_driversquery_stdout():
    with open('tests/driversquery_stdout.csv', 'r', encoding='utf-8') as output:
        result = output.read()
    return result

@patch('driverquery.subprocess.run')
def test_run_driverquery(mock_run):
    # Create a mock subprocess result
    mock_result = Mock()
    mock_result.stdout = get_driversquery_stdout().encode('utf-8')
    mock_run.return_value = mock_result  # Set the return value of mock_run
    # test mock
    assert DriverQuery().get_data() == get_driversquery_stdout()
    # test table format output
    drivers = DriverQuery()
    assert str(drivers) == expected_output_table
    # test csv format output
    drivers = DriverQuery(format_output='CSV')
    assert str(drivers) == expected_output_csv

