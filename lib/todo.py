class Todo:
    def __init__(self):
        self._todo_list = []

    def add_todo_task(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self object
        #   Throws an error if task is not a string
        if type(task) != str:
            raise TypeError("Error: string type is required")
        elif task == '':
            raise Exception("Error: cannot be empty")
        self._todo_list.append(task)
        

    def list_tasks(self):
        # Returns:
        #   List representing all task that needs to be complete
        # Side-effects:
        #   Throws an exception if list is empty
        return self._todo_list

    def complete_task(self, task):
        #Parameters:
        #   task: a string that represents a single task
        #Side-effects:
        #   Finds task in list and deletes it
        #   Throws an error if task is not found
        if self._todo_list.count(task) == 0:
            raise ValueError("Error: task not found in the todo list")
        self._todo_list.remove(task)

