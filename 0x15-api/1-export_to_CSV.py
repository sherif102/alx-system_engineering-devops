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
    employee_name = eval(name_request.read().decode('utf-8'))['name']
    number_of_done_tasks = 0
    total_number_of_tasks = 0
    # task_done_list = []
    # all_tasks = []

    with open(f'{employee_id}.csv', 'w') as file:
        for task in todos:
            # data = f'"{task['userId']}", "{employee_name}", \
            # "{task['completed']}", "{task['title']}"\n'
            data = '"{}", "{}", "{}", "{}"\n'.format(
                task['userId'],
                employee_name,
                task['completed'],
                task['title']
            )
            file.write(data)

    # print(f'Employee {employee_name} is done with tasks'
        #   f'({number_of_done_tasks}/{total_number_of_tasks}):')

    # for task in task_done_list:
    #     print(f'\t {task}')


if __name__ == "__main__":
    todo_getter(argv[1])
