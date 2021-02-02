from demo_function import evaluate
from unittest.mock import patch, call

#to test the evaluate method as it does not have return value for this as in scenario such as 
#person2 dislikes person1 so mocked the let_down_gently() 
@patch('demo_function.send_email')
@patch('demo_function.let_down_gently')
@patch('demo_function.give_it_time')
def test_person2_dislikes_person1(mock_give_it_time, mock_let_down, mock_send_email):

    person1 = 'Bill'
    person2 = {
        'likes':['Sam', 'Joey'],
        'dislikes':['Bill']
    } 

    evaluate(person1, person2)
#as to check whether the mock method is called or not 
    assert mock_let_down.call_count == 1
#check whether the mock method called with specific args 
    mock_let_down.assert_called_once_with(person1)
#as there are others methods which is not called to check the count
    assert mock_give_it_time.call_count == 0
    assert mock_send_email.call_count == 0


#the second sceario is person2 likes person1 as in this case the mock called twice 
#need to verify the it called 2 times and with specific args
@patch('demo_function.send_email')
@patch('demo_function.let_down_gently')
@patch('demo_function.give_it_time')
def test_person2_likes_person1(mock_give_it_time, mock_let_down, mock_send_email):
    person1 = 'Bill'
    person2 = {
        'likes':['Bill'],
        'dislikes':['Sam']
    } 

    evaluate(person1, person2)
#to check it is called with specific args such as person1 and person2 used the call_args_list
    first_call = mock_send_email.call_args_list[0]
    second_call = mock_send_email.call_args_list[1]

    assert first_call == call(person1)
    assert second_call == call(person2)
#to check the mock_end_email called 2 times
    assert mock_send_email.call_count == 2
#the other 2 methods didn't called
    mock_let_down.assert_not_called()
    mock_give_it_time.assert_not_called()

