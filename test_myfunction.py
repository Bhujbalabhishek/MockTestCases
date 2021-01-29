from unittest.mock import call, patch
from myfunction import Calculator


@patch('myfunction.Calculator.fa', autospec=True)
def test_factorial_with_positive_integer(mock_fact):

    #success
    mock_fact.return_value = 6
    res = Calculator.fa(3)
    assert res == 6
    mock_fact.assert_called_with(3)

    #failure
    mock_fact.return_value = None
    res = Calculator.fa('abc')
    assert res is None

    assert mock_fact.call_count == 2
