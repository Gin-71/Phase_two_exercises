"""
Input / output Diagram

add one task => no return
add one task and check the list ==> list[task]
add multiple tasks one by one
add multiple tasks one by one and check the list ==> lista[task1,task2,...]
add multiple tasks all at once and check the list ==> lista[task1,task2,...]

remove one task 
remove one task and check the list
remove multiple tasks one by one
remove multiple tasks one by one and check the list ==> lista[task1,task2,...]
remove multiple tasks all at once and check the list ==> lista[task1,task2,...]
remove a task that is  not in the list ==> raise Eception "That task is not in the list"

Edges cases
add empty task ==> raise Exeption "No task specified"
input with worng format ==> raise Exeption "wrong format"
"""

from lib.task_tracker import *
import pytest

def test_add_one_task():
    my_week = Task_tracker()
    my_week.add_task("Doing a KATA")
    assert my_week.task_list == ["Doing a KATA"]

#def test_add_one_task_and_check_the_list():
#    my_week = Task_tracker()
#    my_week.add_task("Doing a KATA")
#    assert my_week.check_task_list == ["Doing a KATA"]

def test_add_multiple_tasks_one_by_one():
    my_week = Task_tracker()
    my_week.add_task("Doing a KATA")
    my_week.add_task("Finish the second phase")
    my_week.add_task("training")
    my_week.add_task("read 'Good omens'")
    assert my_week.task_list == ["Doing a KATA", "Finish the second phase", "training", "read 'Good omens'"]

def test_add_multiple_task_all_at_once():
    my_week = Task_tracker()
    my_week.add_task("Doing a KATA, Finish the second phase, training, read 'Good omens'")
    assert my_week.task_list == ["Doing a KATA", "Finish the second phase", "training", "read 'Good omens'"]

def test_remove_one_task():
    my_week = Task_tracker()
    my_week.add_task("Doing a KATA")
    my_week .remove_task("Doing a KATA")
    assert my_week.task_list == []

def test_remove_multiple_tasks_one_by_one():
    my_week = Task_tracker()
    my_week.add_task("Doing a KATA")
    my_week.add_task("Finish the second phase")
    my_week.add_task("training")
    my_week.add_task("read 'Good omens'")
    my_week.remove_task("Doing a KATA")
    my_week.remove_task("Finish the second phase")
    my_week.remove_task("training")
    my_week.remove_task("read 'Good omens'")
    assert my_week.task_list == []

def test_remove_multiple_task_all_at_once():
    my_week = Task_tracker()
    my_week.add_task("Doing a KATA, Finish the second phase, training, read 'Good omens'")
    my_week.remove_task("Doing a KATA, Finish the second phase, training, read 'Good omens'")
    assert my_week.task_list == []

def test_remove_task_is_not_in_the_list():
    my_week = Task_tracker()
    my_week.add_task("Doing a KATA, Finish the second phase, training, read 'Good omens'")
    with pytest.raises(Exception) as e:
        my_week.remove_task("call Lore")
    error_message = str(e.value)
    assert error_message == "That task is not in the list"