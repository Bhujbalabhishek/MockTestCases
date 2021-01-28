from unittest.mock import call, patch
from myfunction import Calculator

@patch.object(Calculator, 'sum', autospec = True )
def test_sum(mock_sum):
    mock_sum.return_value = 10
    mock_sum.assert_not_called()
    mock_sum(3,7)
    mock_sum.assert_called_once_with(3,7)
    mock_sum.assert_any_call(3,7)
    mock_sum.assert_called_with(3,7)
    mock_sum.reset_mock()
    assert mock_sum.called == False
    assert mock_sum.return_value == 10

@patch.object(Calculator, 'multiplication', autospec = True)
def test_multiplication(mock_mul):
    mock_mul.return_value = 30
    res = mock_mul(5,6)
    mock_mul.assert_called_once_with(5,6)
    mock_mul.assert_any_call(5,6)

    Calculator.multiplication(1,9)
    mock_mul.assert_any_call(1,9)
    mock_mul.assert_called_with(1,9)
    assert mock_mul.assert_called
    assert mock_mul.call_args == call(1,9)
    assert mock_mul.called == True
    assert mock_mul.return_value == 30
    mock_mul.reset_mock()
    assert mock_mul.called == False
    mock_mul.assert_not_called()

    assert mock_mul.call_count == 0
    mock_mul(2,5)
    mock_mul(6,9)
    assert mock_mul.call_count == 2
    mock_mul.reset_mock()
    mock_mul.side_effect = [
        {'z':54}, {'z':30}
    ]
    re = mock_mul(5, 6)
    assert res == 30

    mock_mul.side_effect = RuntimeError('demo')
    mock_mul(6,9)
    try:
        assert mock_mul.call_args == call(6,9)
    except RuntimeError:
        assert True


@patch('myfunction.Calculator.factorial', return_value = 10)
def test_factorial(mock_fact):
    assert mock_fact.return_value ==10
    assert mock_fact.called == False
    mock_fact(5)
    assert mock_fact.called == True
    assert mock_fact.call_args == call(5)
    mock_fact(8)
    print(mock_fact.mock_calls)
    assert mock_fact.mock_calls == [call(5), call(8)]
    calls = [call(8), call(5)]
    mock_fact.assert_has_calls(calls, any_order=True)

    assert mock_fact.call_count == 2
    mock_fact.assert_called_with(8)
    mock_fact.reset_mock()
    mock_fact.assert_not_called



