#!/usr/bin/python3
"""getting data from an API"""

import json
from sys import argv
from urllib import request


def todo_getter(employee_id):
    """gets the TODO list progress of an employee"""

    req = request.urlopen(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    print(req.status)


if __name__ == "__main__":
    todo_getter(argv[1])
