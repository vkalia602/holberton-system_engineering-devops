#!/usr/bin/python3
'''
Script that takes employee ID and returns information about that employee
'''
import json
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    total_tasks = []
    all_employees = {}
    list_userids = []
    user = argv[1]
    employees = requests.get('{}users/{}'.format(url, user))
    employees = employees.json()
    tasks = requests.get('{}users/{}/todos'
                         .format(url, user))
    tasks = tasks.json()
    for items in tasks:
        total_tasks.append(items)
    all_employees[str(user)] = total_tasks
    file_name = "{}.json".format(user)
    with open(file_name, 'w') as f:
        json.dump(all_employees, f)
