from unittest.mock import patch, call
from datetime import datetime
from demo_function import is_summer, get_now


AUGUST = 8
DECEMBER = 12

#To test whether the Month we are sending as in date is it in summer or not 
#as the month number 6,7,8 is in summer as written the function inside demo_function.
#so The August is in summer and for December is not in summer month as we are mocking the get_now 
@patch('demo_function.get_now')
def test_is_summer_in_august(now_mock):
    now_mock.return_value = datetime(year=2000, month=AUGUST, day=1)
    
    assert is_summer() == True


@patch('demo_function.get_now')
def test_is_summer_in_december(now_mock):
    now_mock.return_value = datetime(year=2000, month=DECEMBER, day=1)
    
    assert is_summer() == False

    assert now_mock.call_count == 1