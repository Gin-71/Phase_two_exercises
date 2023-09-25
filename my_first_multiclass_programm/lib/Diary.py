class Diary:
    def __init__(self, entry):
        if entry == "":
            raise Exception ('Empty entry')
        else:
            self.entry = entry


    def count_words(self):
        #Function: count the amount of words in the diary
        #Input: None
        #Output: words amount(int)
        return len(self.entry.split( ))
