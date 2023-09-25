"""
empty task ==>raise Exception 'An empty task can not be added to the list'
"""

from lib.Task import *
import pytest

def test_empty_task():
    with pytest.raises (Exception) as e:
        today = Task("")
    error_message = str(e.value)
    assert error_message == 'An empty task can not be added to the list'
