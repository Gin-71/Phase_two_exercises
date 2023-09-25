class Task:
    def __init__(self, new_task):
        if new_task == "":
            raise Exception ('An empty task can not be added to the list')
        else:
            self.task = new_task


        
