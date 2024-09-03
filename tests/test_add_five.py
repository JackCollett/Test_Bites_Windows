from lib.add_five import *

def test_add_five_retruns_eight_for_three():
    result = add_five(3)
    assert result == 8