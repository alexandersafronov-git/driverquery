import pytest
from unittest.mock import Mock


def get_driversquery_stdout(filename='tests/driversquery_stdout.csv'):
    with open(filename, 'r', encoding='utf-8') as output:
        result = output.read()
    return result


@pytest.fixture
def mock_driverquery():
    mock_result = Mock()
    mock_result.stdout = get_driversquery_stdout().encode('utf-8')
    return mock_result
