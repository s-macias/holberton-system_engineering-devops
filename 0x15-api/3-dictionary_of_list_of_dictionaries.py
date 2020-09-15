#!/usr/bin/python3
""" Script that, for a given employee ID, returns information about their TODO
list progress exported as a json file """
import json
import requests
from sys import argv


if __name__ == "__main__":
    """ code not executed when imported """
    url = "https://jsonplaceholder.typicode.com/users"
    url_request = requests.get(url)
    todo_list = {}
    for emp in url_request:
        tasks = []
        emp_id = url_request.get('id')
        username = url_request.get('username')
        todos = requests.get("{}/{}/todos".format(url, emp_id)).json()
        for task in todos:
            emp_dic = {}
            emp_dic['username']  = username
            emp_dic['task']  = task.get('title')
            emp_dic['completed'] = task.get('completed')
            tasks.append(emp_dic)
        todo_list[emp_id] = tasks
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(todo_list, jsonfile)
