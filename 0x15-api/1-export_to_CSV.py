#!/usr/bin/python3
"""getting data from an API and export it to CSV"""

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

    with open(f'{employee_id}.csv', 'w') as file:
        for task in todos:
            data = '"{}","{}","{}","{}"\n'.format(
                task['userId'],
                employee_name,
                task['completed'],
                task['title']
            )
            file.write(data)


if __name__ == "__main__":
    todo_getter(argv[1])
