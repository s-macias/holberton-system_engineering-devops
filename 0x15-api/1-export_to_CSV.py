#!/usr/bin/python3
""" Script that, for a given employee ID, returns information about their TODO
list progress exported as a csv file """
import csv
import requests
from sys import argv


if __name__ == "__main__":
    """ code not executed when imported """
    emp = argv[1]
    url_request = "https://jsonplaceholder.typicode.com/users/{}".format(emp)
    url = requests.get(url_request)
    todos = requests.get("{}/todos".format(url_request)).json()
    emp_name = url.json().get('name')
    with open("{}.csv".format(emp), "w") as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for task in todos:
            row = [emp, emp_name, task.get('completed'), task.get('title')]
            writer.writerow(row)
