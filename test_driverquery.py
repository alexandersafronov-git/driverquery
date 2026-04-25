from unittest.mock import patch
from driverquery import DriverQuery
import pytest
from conftest import get_driversquery_stdout

expected_output_table = """Module Name    Display Name    Driver Type    Link Date
-------------  --------------  -------------  -----------
AppvStrm       AppvStrm        File System"""

expected_output_csv = """"Module Name","Display Name","Driver Type","Link Date"
"AppvStrm","AppvStrm","File System ",""
"""


@patch('driverquery.subprocess.run')
def test_run_driverquery(mock_run, mock_driverquery):
    # Create a mock subprocess result
    mock_run.return_value = mock_driverquery
    # test mock
    assert DriverQuery().get_data() == get_driversquery_stdout()


@patch('driverquery.subprocess.run')
def test_driverquery_table(mock_run, mock_driverquery):
    # test table format output
    mock_run.return_value = mock_driverquery
    drivers = DriverQuery()
    assert str(drivers) == expected_output_table

@patch('driverquery.subprocess.run')
def test_driverquery_csv(mock_run, mock_driverquery):
    # test csv format output
    mock_run.return_value = mock_driverquery
    drivers = DriverQuery(format_output='CSV')
    assert str(drivers) == expected_output_csv

@patch('driverquery.subprocess.run')
def test_driverquery_wrong_format_output(mock_run, mock_driverquery):
    # test wrong output format
    mock_run.return_value = mock_driverquery
    drivers = DriverQuery(format_output='UNKNOWN')
    with pytest.raises(Exception) as e_info:
        str(drivers)

