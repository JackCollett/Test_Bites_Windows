from lib.greet import *

def test_greet_name_of_john():
    result = greet("john")
    assert result == "Hello, john"