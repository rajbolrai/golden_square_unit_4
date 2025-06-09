from lib.todo import *
import pytest

"""
Adding non-string task
raises an type error
"""
def test_given_non_string_task_raise_type_error():
    obj_todo = Todo()
    with pytest.raises(TypeError) as err:
        obj_todo.add_todo_task(12123)
    error_message = str(err.value)
    assert error_message == "Error: string type is required"

"""
Given an an empty task
raises an exception
"""
def test_given_empty_task_raise_exception():
    obj_todo = Todo()
    with pytest.raises(Exception) as err:
        obj_todo.add_todo_task('')
    error_message = str(err.value)
    assert error_message == "Error: cannot be empty"

"""
Adding a task
updates the todo list
"""
def test_added_task_output_updated_task_list():
    obj_todo = Todo()
    obj_todo.add_todo_task("Walk the dog")
    assert obj_todo.list_tasks() == ["Walk the dog"]
    
"""
Adding a multiple tasks
updates the todo list
"""
def test_added_multiple_task_output_updated_task_list():
    obj_todo = Todo()
    obj_todo.add_todo_task("Walk the dog")
    obj_todo.add_todo_task("Walk the cat")
    obj_todo.add_todo_task("Walk the snake")
    obj_todo.add_todo_task("Walk the spider")
    
    assert obj_todo.list_tasks() == ["Walk the dog","Walk the cat", "Walk the snake", "Walk the spider"]
"""
Adding a task and completing that task 
removes task from the todo list
"""
def test_add_and_complete_tasks_removes_task_from_todo_list():
    obj_todo = Todo()
    obj_todo.add_todo_task("Walk the dragon")
    obj_todo.add_todo_task("Walk the tree")
    obj_todo.add_todo_task("Walk the horse")
    obj_todo.complete_task("Walk the dragon")
    assert obj_todo.list_tasks() == ["Walk the tree", "Walk the horse"]

"""
completing task that is not in the todo list
raises an value error
"""
def test_given_unverified_task_to_complete_output_value_error():
    obj_todo = Todo()
    with pytest.raises(ValueError) as err:
        obj_todo.complete_task("Walk the cat")
    error_message = str(err.value)
    assert error_message == "Error: task not found in the todo list"
