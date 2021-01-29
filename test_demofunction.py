from unittest.mock import patch, call
from datetime import datetime
from demo_function import is_summer, get_now


AUGUST = 8
DECEMBER = 12

@patch('demo_function.get_now')
def test_is_summer_in_august(now_mock):
    now_mock.return_value = datetime(year=2000, month=AUGUST, day=1)
    
    assert is_summer() == True


@patch('demo_function.get_now')
def test_is_summer_in_december(now_mock):
    now_mock.return_value = datetime(year=2000, month=DECEMBER, day=1)
    
    assert is_summer() == False

    assert now_mock.call_count == 1