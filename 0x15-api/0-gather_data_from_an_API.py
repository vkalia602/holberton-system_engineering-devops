#!/usr/bin/python3
'''
Script that takes employee ID and returns information about that employee
'''

import requests
from sys import argv


if __name__ == "__main__":
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    completed_tasks = []
    employee = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(argv[1]))
    tasks = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                         .format(argv[1]))
    tasks = tasks.json()
    employee = employee.json()
    for todo_dict in tasks:
        if todo_dict.get('completed') is True:
            completed_tasks.append(todo_dict.get('title'))
            NUMBER_OF_DONE_TASKS += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(employee.get('name'), NUMBER_OF_DONE_TASKS,
                  len(tasks)))
    for TASK_TITLE in completed_tasks:
        print('\t {}'. format(TASK_TITLE))
