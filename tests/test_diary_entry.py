from lib.diary_entry import Diary
"""
a diary exist when created with a title and contents
"""
def test_diary_exists_when_one_is_created():
    diary = Diary("My Diary", "This is the contents of my diary")
    assert diary.__dict__ == {'_contents': 'This is the contents of my diary', '_read_so_far': 0, '_title': 'My Diary'}

"""
when format method is called it return a formatted diary entry
"""
def test_format_method():
    diary = Diary("My Diary", "This is the contents of my diary")
    result = diary.format()
    assert result == "My Diary: This is the contents of my diary"

"""
when count_words is called it return the number of words in the diary entry
"""
def test_count_words():
    diary = Diary("My Diary", "This is the contents of my diary")
    result = diary.count_words()
    assert result == 7

"""
given a an integer representing the nyumber of words the user can read per minute
the reading_time method returns an estimate of the reading time in minutes
for the content of the diary
"""
def test_reading_time():
    diary = Diary("My Diary", "This is the contents of my diary")
    result = diary.reading_time(10)
    assert result == 1

"""
given an addition parameter of an integer representing minutes the use has to read
return a string representing the chunck of content the user can read in that time
"""
def test_reading_chunks():
    diary = Diary("My Diary", "This is the contents of my diary")
    result = diary.reading_chunk(1, 2)
    assert result == "This is"
    result2 = diary.reading_chunk(1, 2)
    assert result2 == "the contents"