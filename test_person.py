from unittest.mock import patch, call
from person import get_next_person

#mock the get_random_person() function which is calling the fake API as the testcase is for a newuser as it doesnot see
#any names so setting up the return value and checking whether it is correct or not.
@patch('person.get_random_person')
def test_new_person(mock_random):

    user = {'name':[]}
    expected_person = 'demo'

    mock_random.return_value = 'demo'

    actual_person = get_next_person(user)

    assert expected_person == actual_person


#to test the method which is inside the while loop as it called multiple times
#for each time it should return different values so need to use the side effect to return 
#different values each time.
@patch('person.get_random_person')
def test_experinced_person(mock_random):

    user = {'name':['sara', 'anushka']}
    expected_person = 'katie'

    mock_random.side_effect = ['sara', 'anushka', 'katie']

    actual_person = get_next_person(user)

    assert expected_person == actual_person

    mock_random.assert_called()
    assert mock_random.call_count == 3