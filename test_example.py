from unittest import TestCase, mock, main
from example import get_number


@mock.patch('example.randint')
def test_get_number_with_even_number(randint_mock):
    randint_mock.return_value = 42
    result = get_number()
    assert 'Even number: 42' == result
    
@mock.patch('example.randint')
def test_get_number_with_odd_number(randint_mock):
    randint_mock.return_value = 69
    result = get_number()
    assert 'Odd number: 69' == result
