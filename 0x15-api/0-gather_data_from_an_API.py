#!/usr/bin/python3
"""get todo list using rest api"""
if __name__ == '__main__':
    import json
    import requests
    import sys
    id = sys.argv[1]
    tasks = []
    resp = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}/')
    resp = resp.json()
    name = resp.get("name")
    resp = requests.get('https://jsonplaceholder.typicode.com'
                        f'/users/{id}/todos/')
    resp = resp.json()
    total = 0
    done = 0
    for task in resp:
        total += 1
        if (task.get("completed")):
            tasks.append(task.get("title"))
            done += 1
    print(f'Employee {name} is done with tasks({done}/{total}):')
    for task in tasks:
        print(f'\t {task}')
