"""
1. the problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

add strings, store and return a list

2. Class Interface design
"""

class Music_tracker:
    def __init__(self):
        #list of songs
        self.listened_songs =[]
    

    def add_song(self, song):
        #Funtion: adding a song
        #Input: the name of the song to add, type string
        #Output: no outputs
        if song == "":
            raise Exception ("Invalid entry")
        else:    
            self.listened_songs.append(song)
    
    def add_several_songs(self, songs):
        several_songs = songs.split(", ")
        for string in several_songs:
            if "and" not in string:
                self.listened_songs.append(string)
            else:
                lasts_songs = string.replace(" and ", ", ")
                self.add_several_songs(lasts_songs)

    def songs_list(self):
        #Funtion: adding a song
        #Inputs: No inputs required
        #Output: return the list of songs
        return self.listened_songs