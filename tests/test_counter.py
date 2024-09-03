from lib.counter import *

def test_counter_start_with_zero():
    result = Counter()
    assert result.count == 0

def test_counter_added_five():
    result = Counter()
    result.add(5)
    assert result.report() == "Counted to 5 so far."

'''
When we add mulitple numbers to the counter
The sum of thos enumbers is the final count
'''
def test_counter_with_multiple_numbers_to_the_count():
    counter = Counter()
    counter.add(1)
    counter.add(5)
    assert counter.report() == "Counted to 6 so far."