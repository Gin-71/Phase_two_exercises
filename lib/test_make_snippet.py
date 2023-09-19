from lib.make_snippet import *
import pytest

def test_empty_string():
    result = make_snippet("")
    assert result ==""

def test_less_than_five_words():
    result = make_snippet("Once upon a time")
    assert result == "Once upon a time"

def test_more_than_five_words():
    result = make_snippet('By failing to prepare, one is preparing to fail')
    assert result == 'By failing to prepare, one...'