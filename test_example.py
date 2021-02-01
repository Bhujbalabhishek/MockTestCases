from unittest import mock, call
from example import get_number

#As mocking the randint function as to check wheter the number is even or odd
@mock.patch('example.randint')
def test_get_number_with_even_number(randint_mock):
    randint_mock.return_value = 42
    result = get_number()
    assert 'Even number: 42' == result
    
@mock.patch('example.randint')
def test_get_number_with_odd_number(randint_mock):
    randint_mock.return_value = 59
    result = get_number()
    assert 'Odd number: 59' == result
    randint_mock.assert_called_with(1,100)
    assert randint_mock.mock_calls == [call(1,100)]
