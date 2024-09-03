from lib.check_codeword import *

def test_correct_codeword():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_close_codeword():
    result = check_codeword("home")
    assert result == "Close, but nope"

def test_incorrect_codeword():
    result = check_codeword("rabbit")
    assert result == "WRONG!"