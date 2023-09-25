from lib.Agenda import *
from lib.Diary import *
from lib.Task import *
import pytest

"""
add one new diary entry without contacts==> diarylist = [new diary entry]
"""
def  test_add_one_entry_no_contacts():
    my_week = Agenda()
    my_week.add_diary_entry("I have so much to do today")
    one_entry = [new_entries for new_entries in my_week.diary_entries]
#week_tasks = [new_task.task for new_task in week_list.incomplete()] 
    assert my_week.diary_entries == one_entry

"""
add two new diary entries without contacts ==>diarylist = [new diary entry 1, new diary entry 2]
"""

def test_add_two_entries_no_contacts():
    my_week = Agenda()
    my_week.add_diary_entry("I have so much to do today")
    my_week.add_diary_entry("And I want sleep so baddly")
    one_entry = [new_entries for new_entries in my_week.diary_entries]
    assert my_week.diary_entries == one_entry

"""
add one entry with one contact ==> diarylist = [new diary entry], contacs = [phone number]
"""

def  test_add_one_entry_one_contacts():
    my_week = Agenda()
    my_week.add_diary_entry("I have so much to do today 7911123456")
    assert my_week.contacts == ["7911123456"]

"""
add one entries with two contacts ==> [new diary entry], contacs = [phone number 1, phone number 2]
"""
def  test_add_one_entry_two_contacts():
    my_week = Agenda()
    my_week.add_diary_entry("I have so much to do today contact:7911123456, other contact: 7911123455")
    assert my_week.contacts == ["7911123456","7911123455"]

"""
add two entries with one contac each ==> diarylist = [new diary entry], contacs = [phone number 1, phone number 2]
"""
def test_add_two_entries_two_contacts():
    my_week = Agenda()
    my_week.add_diary_entry("I have so much to do today, 7911123456")
    my_week.add_diary_entry("7911123455 And I want sleep so baddly")
    assert my_week.contacts == ["7911123456","7911123455"]

"""
add two entries, one with one contact ==> [new diary entry], contacs = [phone number 1]
"""
def test_add_two_entries_one_contacts():
    my_week = Agenda()
    my_week.add_diary_entry("I have so much to do today")
    my_week.add_diary_entry("And I want sleep so baddly")
    one_entry = [new_entries for new_entries in my_week.diary_entries]
    assert my_week.diary_entries == one_entry

"""
add one entry with nombers but not contact ==> [new diary entry], contacs = []
"""

def  test_add_one_entry_two_wrong_length_numbers():
    my_week = Agenda()
    my_week.add_diary_entry("I have so much to do today contact:79111456, other contact: 79111234")
    assert my_week.contacts == []

"""
show past entries with one entry added = [new diary entry]
"""

def test_show_past_entries_with_one_entry_added():
    my_week = Agenda()
    my_week.add_diary_entry("I have so much to do today contact:79111456, other contact: 79111234")
    one_entry = [new_entries for new_entries in my_week.diary_entries]
    assert my_week.get_past_entries() == one_entry

"""
show past entries with two entries added = [new diary entry 1, new diary entry 2]
"""
def test_show_past_entries_with_two_entries_added():
    my_week = Agenda()
    my_week.add_diary_entry("I have so much to do today contact:79111456, other contact: 79111234")
    my_week.add_diary_entry("And I want sleep so badly")
    one_entry = [new_entries for new_entries in my_week.diary_entries]
    assert my_week.get_past_entries() == one_entry

""""
show past entries with no previous esntries = 'No previous entries'
"""
def test_show_past_entries_with_no_previous_entries():
    my_week = Agenda()
    one_entry = [new_entries for new_entries in my_week.diary_entries]
    assert my_week.get_past_entries() == 'No previous entries'

"""
read now with one useful entry ==> list [one entry]
"""
def test_read_now_with_one_useful_entry():
    my_week = Agenda()
    my_week.add_diary_entry("I have so much to do today contact: 79111456, other contact: 79111234")
    one_entry = [new_entries for new_entries in my_week.diary_entries]
    assert my_week.read_now(10, 2) == one_entry

"""
read now with one long entry ==> 'No entries short enough'
"""
def test_read_now_with_no_viable_entries():
    my_week = Agenda()
    my_week.add_diary_entry("I have so much to do today contact: 79111456, other contact: 79111234")
    assert my_week.read_now(1, 2) == 'No entries short enough'

"""
read now with two useful entries ==> list [entry one, entry two]
"""

def test_read_now_with_two_entries_added():
    my_week = Agenda()
    my_week.add_diary_entry("I have so much to do today contact:79111456, other contact: 79111234")
    my_week.add_diary_entry("And I want sleep so badly")
    one_entry = [new_entries for new_entries in my_week.diary_entries]
    assert my_week.read_now(10, 2) == one_entry

"""
read now with two entries one useful ==> list[useful entry]
"""

def test_read_now_with_two_entries_added_but_one_viable():
    my_week = Agenda()
    my_week.add_diary_entry("I have so much to do today contact:79111456, other contact: 79111234")
    my_week.add_diary_entry("And I want sleep so badly")
    one_entry = [new_entries for new_entries in my_week.diary_entries]
    assert my_week.read_now(4, 2) == [one_entry[1]]

"""
read now with two long entries ==> 'No entries short enough'
"""

def test_read_now_with_two_entries_added_but_none_short_enough():
    my_week = Agenda()
    my_week.add_diary_entry("I have so much to do today contact:79111456, other contact: 79111234")
    my_week.add_diary_entry("And I want sleep so badly")
    one_entry = [new_entries for new_entries in my_week.diary_entries]
    assert my_week.read_now(1, 2) == "No entries short enough"

"""
read now with no entries ==> 'Not entries avaible'
"""
def test_read_now_with_no_entries_added():
    my_week = Agenda()
    assert my_week.read_now(1, 2) == "No entries added"

"""
add one task ==> task_list == [one task]
"""
def test_add_one_task():
    my_week = Agenda()
    my_week.add_task("finish phase 2")
    one_entry = [new_entries for new_entries in my_week.task_list]
    assert my_week.task_list == one_entry

"""
add two tasks ==> todo_list == [task one, task two]
"""
def test_add_two_tasks():
    my_week = Agenda()
    my_week.add_task("finish phase 2")
    my_week.add_task("start phase 3")
    one_entry = [new_entries for new_entries in my_week.task_list]
    assert my_week.get_todo_list() == one_entry

"""
empty string as entry ==> raise Exception 'This entry is not valid'
"""

def test_empty_string_as_diary_entry():
    my_week = Agenda()
    with pytest.raises(Exception) as e:
        my_week.add_diary_entry("")
    error_message = str(e.value)
    assert error_message == 'Empty entry'

"""
wrong type task ==> raise Exception 'A task should be a string'
"""

def test_wrong_type_entry_for_a_task():
    my_week = Agenda()
    with pytest.raises(Exception) as e:
        my_week.add_task(12345)
    error_message = str(e.value)
    assert error_message == 'A task should be type string'

"""
wrong type wpm ==> raise Exception 'A task shoild be a int'
"""

def test_wrong_type_entry_for_a_wpm():
    my_week = Agenda()
    with pytest.raises(Exception) as e:
        my_week.read_now("a couple of words", 4)
    error_message = str(e.value)
    assert error_message == 'Wpm should be type int'
