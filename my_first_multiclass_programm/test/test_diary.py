"""
entry with 10 words ==> 10
"""

"""
empty entry ==>raise Exception 'Empty entry'
"""

from lib.Diary import *
import pytest 


def test_ten_words_entry():
    today = Diary("Today is Monday, first day of the week. Tan Tan.")
    assert today.count_words() == 10

def test_empty_entry():
    with pytest.raises (Exception) as e:
        today = Diary("")
    error_message = str(e.value)
    assert error_message == 'Empty entry'
