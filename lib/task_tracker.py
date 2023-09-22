"""
As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

--------------------------

1.  Name: Task_tracker
    add, store and remove strings

"""

class Task_tracker():

    def __init__(self):
        self.task_list = []
        pass

    def add_task(self,task):
        #add the task to the list
        #public method
        #Inputs: task type str
        #Outputs: return the list of tasks updated
        new_task = task.split(", ")
        self.task_list = self.task_list + new_task
        return self.task_list
    
    def check_task_list(self):
        #show the task list to the user
        #private method
        #no input
        #Outputs: return the current list of tasks 
        current_list = self.task_list
        return current_list

    def remove_task(self,task):
        #remove the task from the list
        #public method
        #Inputs: task type str
        #Outputs: return the list of tasks updated
        if task not in self.task_list:

            
            tasks_to_remove = task.split(", ")
            for task_to_remove in tasks_to_remove:
                self.task_list.remove(task_to_remove)
            return self.task_list
        else:
            raise Exception ("That task is not in the list")