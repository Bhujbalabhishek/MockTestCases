from unittest.mock import patch
from demo import sum

@patch('demo.divide')
@patch('demo.multiplication')
def test_for_multiplication(mock_mul, mock_div):
    res = sum(51)

    mock_mul.assert_called_with()
    assert mock_mul.call_count == 1

    mock_div.assert_not_called()
    assert mock_div.call_count == 0


@patch('demo.divide')
@patch('demo.multiplication')
def test_for_divide(mock_mul, mock_div):
    res = sum(50)

    mock_mul.assert_not_called()
    assert mock_mul.call_count == 0

    mock_div.assert_called()
    assert mock_div.call_count == 1