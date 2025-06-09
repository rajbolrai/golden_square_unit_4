# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class Todo:
    def __init__(self):
        pass

    def add_todo_task(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self object
        #   Throws an error if task is not a string
        pass # No code here yet

    def list_tasks(self):
        # Returns:
        #   List representing all task that needs to be complete
        # Side-effects:
        #   Throws an exception if list is empty
        pass

    def complete_task(self, task);
        #Parameters:
        #   task: a string that represents a single task
        #Side-effects:
        #   Finds task in list and deletes it
        #   Throws an error if task is not found
        pass


    
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Adding non-string task
raises an type error
"""
obj_todo = Todo()
obj_todo.add_todo_task(12123) #== "Error: tasks are string only


"""
Given an an empty task
raises an exception
"""
obj_todo = Todo()
obj_todo.add_todo_task('') #== "Error: task cannot be empty

"""
Adding a task
updates the todo list
"""
obj_todo = Todo()
obj_todo.add_todo_task("Walk the dog")
obj_todo.list_tasks() # => ["Walk the dog"]

"""
Adding a task and completing that task 
removes task from the todo list
"""
obj_todo = Todo()
obj_todo.add_todo_task("Walk the dog")
obj_todo.complete_task("Walk the dog")
obj_todo.list_tasks() # => []

"""
completing task that is not in the todo list
raises an value error
"""
obj_todo = Todo()
obj_todo.add_todo_task("Walk the dog")
obj_todo.complete_task("Walk the cat") # == "Error: Not found in the todo list"

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
