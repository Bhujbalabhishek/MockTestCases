from unittest.mock import Mock, patch, call
from example import get_json

#first scenario is to test get valid json so for that open() return File object
#open(filename).read() so we need to mock the File.read() but its and instance 
#so the mock_open return an another mock_file which is mock

@patch('builtins.open')
def test_get_valid_json(mock_open):
    filename = 'demo.json'
#create a Mock and that mock will call read method and retruns a json
    mock_file = Mock()
#mocking the read method
    mock_file.read.return_value = '{"foo":"bar"}'

#the mock_open return value is another mock which we have created which return a actual json
    mock_open.return_value = mock_file

    actual_result = get_json(filename)
#checking whether it return valid json or not 
    assert actual_result == {"foo":"bar"}
     

#test whether file is missing so use side effect for that to raise IOError
@patch('builtins.open')
def test_get_json_ioerror(mock_open):
    filename = 'demo.json' 

    mock_open.side_effect = IOError

    actual_result = get_json(filename)
#to check wheter the actual result should be None
    assert None == actual_result

#mock_loads calls it throws an ValueError as we are used side_effect
@patch('builtins.open')
@patch('json.loads')
def test_get_json_valueerror(mock_loads, mock_open):
    filename = 'demo.json'

    mock_file = Mock()
    mock_file.read.return_value = '{"foo":"bar"}'
    mock_open.return_value = mock_file

    mock_loads.side_effect = ValueError 

    actual_result = get_json(filename)
#to check wheter the actual result should be None
    assert None == actual_result 
    