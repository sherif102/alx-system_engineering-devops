#!/usr/bin/python3
"""getting data from an API and export it to JSON"""

import json
from urllib import request


def todo_getter(employee_id):
    """gets the TODO list progress of an employee"""

    name_request = request.urlopen(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    todos = request.urlopen(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')

    todos = json.loads(todos.read().decode('utf-8'))
    employee_name = eval(name_request.read().decode('utf-8'))
    employee_data = []

    for task in todos:
        employee_data.append({
            "username": employee_name['username'],
            "task": task['title'],
            "completed": task["completed"]
        })
    return [employee_name['id'], employee_data]


all_user_data = {}


def all_todo_getter():
    """gets TODO for all the users"""
    counter = 1
    try:
        while request.urlopen(
                f'https://jsonplaceholder.typicode.com/users/{counter}'):
            all_user_data[todo_getter(counter)[0]] = todo_getter(counter)[1]
            counter += 1
    except Exception:
        with open('todo_all_employees.json', 'w') as file:
            json.dump(all_user_data, file)


if __name__ == "__main__":
    all_todo_getter()
