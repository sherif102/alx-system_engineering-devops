#!/usr/bin/python3
"""getting data from an API"""

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
    employee_name = eval(name_request.read().decode('utf-8'))['name']
    number_of_done_tasks = 0
    total_number_of_tasks = 0
    task_done_list = []

    for task in todos:
        if task['completed'] is True:
            number_of_done_tasks += 1
            task_done_list.append(task['title'])
        total_number_of_tasks += 1

    print(f'Employee {employee_name} is done with tasks '
          f'({number_of_done_tasks}/{total_number_of_tasks}):')

    for task in task_done_list:
        print(f'\t {task}')


if __name__ == "__main__":
    todo_getter(argv[1])
