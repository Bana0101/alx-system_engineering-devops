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
    with open('{}.csv'.format(id), 'w', newline='') as csvfile:
        for task in resp:
            status = task["completed"]
            title = task["title"]
            csvfile.write(f'"{id}","{username}","{status}","{title}"\n')

# new test
