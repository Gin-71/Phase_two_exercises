from lib.Diary import *
from lib.Task import *
class Agenda:
    def __init__(self):
        self.diary_entries = []
        self.task_list = []
        self.contacts = []
        pass

    def add_diary_entry(self, new_entry):
        #Function: add a new diary entry and check for mobile numbers
        #input: new_entry, type str
        #output: None
        #side effects: create a new diary object and add mobile numbers
        #               to contacts list if it applies 
        new_diary_entry = Diary(new_entry)
        possible_number = ""
        if new_entry == "":
            raise Exception('This entry is not valid')
        else:
            for index in range(len(new_entry)-9):
                if new_entry[index] in "0123456789":
                    possible_number = new_entry[index:index+10]
                for item in possible_number:
                    if item not in "0123456789":
                        possible_number = ""
                if possible_number != "":
                    self.contacts.append(possible_number)

            self.diary_entries.append(new_diary_entry)

    def get_past_entries(self):
        #Function: show all the entries previously added
        #input: None
        #Output: return the past entries as a list of diary objects
        if self.diary_entries == []:
            return "No previous entries"
        else:
            return self.diary_entries
    
        
    def read_now(self, wpm, minutes):
        #Function: show a entry the user can read in a defined time
        #Inputs: wpm(type int), minutes(type int)
        #Output: ideal entry for the time (type diary)
        readable_words = wpm * minutes
        readable_entries = []
        if (type(wpm) == int) and (type(minutes) == int):
            if self.diary_entries == []:
                return "No entries added"
            else:
                for entry in self.diary_entries:
                    wordcount = entry.count_words()
                    if wordcount <= readable_words:
                        readable_entries.append(entry)
                if len(readable_entries) == 0:
                    return 'No entries short enough'
                else:
                    return readable_entries
        elif (type(wpm) != int) and (type(minutes) == int):
            raise Exception ('Wpm should be type int')
        elif (type(wpm) != int) and (type(minutes) == int):
            raise Exception ('Minutes should be type int')
        else:
            raise Exception ("Wpm and minutes should be type int")
        

    def add_task(self, new_task):
        #Funtion: add a new_task to the todo list
        #Input: new_task (type str)
        #Output: None
        #side effects: create a new task object
        if type(new_task) == str:
            task = Task(new_task)
            self.task_list.append(task)
        else:
            raise Exception('A task should be type string')

    def get_todo_list(self):
        #Input: None
        #Output: return a list of added task (type: list of tasks)
        return self.task_list

    def get_contacts(self):
        #Function: show the contact list
        #Input: None
        #Otuput: return a list of added contacts(Type:list of strings)
        pass

