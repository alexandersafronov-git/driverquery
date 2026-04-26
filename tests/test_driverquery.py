from unittest.mock import patch
from ..driverquery import DriverQuery
import pytest
from .conftest import get_driversquery_stdout


@patch('subprocess.run')
def test_run_driverquery(mock_run, mock_driverquery):
    # Create a mock subprocess result
    mock_run.return_value = mock_driverquery
    # test mock
    assert DriverQuery().get_data() == get_driversquery_stdout()


@patch('subprocess.run')
@pytest.mark.parametrize("format_output,expected", [("TABLE", "tests/expected_output_table.txt"),
                                                    ("CSV", 'tests/expected_output.csv')])
def test_driverquery_output(mock_run, mock_driverquery, format_output, expected):
    # test table format output
    mock_run.return_value = mock_driverquery
    drivers = DriverQuery(format_output=format_output)
    assert str(drivers).replace('\r', '') == str(get_driversquery_stdout(expected))


@patch('subprocess.run')
def test_driverquery_wrong_format_output(mock_run, mock_driverquery):
    # test wrong output format
    mock_run.return_value = mock_driverquery
    drivers = DriverQuery(format_output='UNKNOWN')
    with pytest.raises(Exception) as e_info:
        str(drivers)
