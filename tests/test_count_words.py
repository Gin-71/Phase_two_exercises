from lib.count_words import *
import pytest

def test_empty_string():
    result = count_words("")
    assert result == 0

def test_count_words():
    result = count_words("Once upon a time")
    assert result == 4
