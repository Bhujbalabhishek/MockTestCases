from unittest.mock import patch
from sample import fa
import math

@patch('math.factorial')
def test_fa_valid_value(mock_fact):
    res = fa(5)

    mock_fact.assert_called
    mock_fact.assert_called_with(5)

    assert mock_fact.call_count == 1

@patch('math.factorial')
def test_fa_invalid_value(mock_fact):
    res = fa(-4)

    mock_fact.assert_not_called
    assert mock_fact.call_count == 0

    assert res == None