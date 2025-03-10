#!/usr/bin/python3
"""getting data from an API and export it to JSON"""

import json
from sys import argv
from urllib import request


def todo_getter(employee_id):
    """gets the TODO list progress of an employee"""

    name_request = request.urlopen(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    todos = request.urlopen(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')

    todos = json.loads(todos.read().decode('utf-8'))
    employee_name = eval(name_request.read().decode('utf-8'))['username']
    employee_data = []

    for task in todos:
        employee_data.append({
            "task": task['title'],
            "completed": task["completed"],
            "username": employee_name,
        })

    data = {f'{employee_id}': employee_data}

    with open(f'{employee_id}.json', 'w') as file:
        json.dump(data, file)


if __name__ == "__main__":
    todo_getter(argv[1])
