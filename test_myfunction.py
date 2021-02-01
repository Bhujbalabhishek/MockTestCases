from unittest.mock import call, patch
from myfunction import fa

#mocking the factorial function if value is less  than 0 it return None or return the Factorial of number. 
@patch('myfunction.math.factorial', autospec=True)
def test_factorial_with_positive_integer(mock_fact):

    #success
    mock_fact.return_value = 6
    res = fa(3)
    assert res == 6


    #failure
    mock_fact.return_value = None
    res = fa(-5)
    assert res is None
    
    mock_fact.assert_called_with(3)
    mock_fact.has_calls = [call(3)]

    assert mock_fact.call_count == 1
