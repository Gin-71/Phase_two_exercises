"""
3. Example tests

Input / output diagram

add "one song" ==> no return / listened_songs = ["one song"]

add "song one" and "song two" one by one ==> no return 
/ listened_songs = ["one song","song two"]

add "song one" and "song two" at the same time ==> no return
/ listened_songs = ["one song","song two"]

add "song one", "song two" and "song three" at the same time
==> no return / / listened_songs = ["one song","song two",
"song three]

see the list of listened songs ==> ["one song","song two",
"song three]

Edge cases

empty string ==> doesn't matter because is still and string 
and coul be the name of a song, but if is no a song it should 
raise an Exception
"""

from lib.music_tracker import *
import pytest

def test_add_one_song():
    my_music = Music_tracker()
    my_music.add_song("one song")
    assert my_music.listened_songs == ["one song"]

def test_add_two_songs_one_by_one():
    my_music = Music_tracker()
    my_music.add_song("song one")
    my_music.add_song("song two")
    assert my_music.listened_songs == ["song one", "song two"]

def test_add_two_songs_at_same_time():
    my_music = Music_tracker()
    my_music.add_several_songs("song one and song two")
    assert my_music.listened_songs == ["song one", "song two"]

def test_add_three_songs_at_the_same_time():
    my_music =Music_tracker()
    my_music.add_several_songs("song one, song two and song three")
    assert my_music.listened_songs == ["song one", "song two", "song three"]

def test_access_to_listened_songs():
    my_music = Music_tracker()
    my_music.add_several_songs("song one, song two and song three")
    assert my_music.songs_list() == ["song one", "song two", "song three"]

def test_empty_input():
    my_music = Music_tracker()
    with pytest.raises(Exception) as e:
        my_music.add_song("")
    error_message = str(e.value)
    assert error_message == "Invalid entry"
    