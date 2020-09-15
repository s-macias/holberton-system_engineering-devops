#!/usr/bin/python3
""" Script that, for a given employee ID, returns information about their TODO
list progress. """
import requests
from sys import argv


if __name__ == "__main__":
    """ code not executed when imported """
    emp_id = argv[1]
    emp_name = requests.get(
             "https://jsonplaceholder.typicode.com/users/{}".format(
                  emp_id))
    todos = requests.get(
              "https://jsonplaceholder.typicode.com/todos?emp_id={}".format(
                  emp_id))
    todos = todos.json()
    emp_name = emp_name.json()

    done_tasks = 0
    total = 0
    todo_list = []
    for task in todos:
        total += 1
        if task.get('completed'):
            done_tasks += 1
            todo_list.append(task.get("title"))

    print("Employee {} is done with tasks:({}/{}):".format(
            emp_name.get("name"), done_tasks, total))
    for task in todo_list:
        print("\t {}".format(task))
