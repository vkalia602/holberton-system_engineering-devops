#!/usr/bin/python3
'''
Script that takes employee ID and returns information about that employee
'''

import requests
from sys import argv


if __name__ == "__main__":
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    total_tasks = []
    employee = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(argv[1]))
    tasks = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                         .format(argv[1]))
    tasks = tasks.json()
    employee = employee.json()

    file_name = "{}.csv".format(tasks[0].get('userId'))
    with open(file_name, 'w') as f:
        for items in tasks:
            f.write('"{}","{}","{}","{}"'.
                    format(items.get('userId'), employee.get('username'),
                           items.get('completed'), items.get('title')))
            f.write("\n")
