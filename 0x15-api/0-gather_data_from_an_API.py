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
        if todo_dict['completed'] is True:
            completed_tasks.append(todo_dict['title'])
            NUMBER_OF_DONE_TASKS += 1
        TOTAL_NUMBER_OF_TASKS += 1
    print('Employee {} is done with tasks ({}/{}):'
          .format(employee['name'], NUMBER_OF_DONE_TASKS,
                  TOTAL_NUMBER_OF_TASKS))
    for items in completed_tasks:
        print('\t', format(items))
