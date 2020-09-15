#!/usr/bin/python3
""" Script that, for a given employee ID, returns information about their TODO
list progress in a JSON file """
import json
import requests
from sys import argv


if __name__ == "__main__":
    """ code not executed when imported """
    emp = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(emp)
    url_request = requests.get(url)
    todos = requests.get("{}/todos".format(url)).json()
    username = url_request.json().get('name')
    todo_list = []
    emp_dict = {}
    for task in todos:
        tasks = {}
        tasks['task'] = task.get('title')
        tasks['completed'] = task.get('completed')
        tasks['username'] = username
        todo_list.append(tasks)
    emp_dict[emp] = todo_list
    with open("{}.json".format(emp), "w") as jsonfile:
        json.dump(emp_dict, jsonfile)
