#!/usr/bin/python3
"""get todo list using rest api"""
if __name__ == '__main__':
    import json
    import requests
    import sys
    import csv
    id = sys.argv[1]
    resp = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}/')
    resp = resp.json()
    username = resp.get("username")
    resp = requests.get('https://jsonplaceholder.typicode.com'
                        f'/users/{id}/todos/')
    resp = resp.json()
    new_dict = {
            id: [
                {
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": username
                    } for task in resp
                ]
            }
    with open('{}.json'.format(id), 'w') as jsonfile:
        json.dump(new_dict, jsonfile)
