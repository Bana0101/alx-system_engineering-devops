#!/usr/bin/python3
"""get todo list using rest api export to json"""
if __name__ == '__main__':
    import json
    import requests
    resp = requests.get(f'https://jsonplaceholder.typicode.com/users/')
    resp = resp.json()
    all_user_dict = {}
    for user in resp:
        id = user.get("id")
        resp_task = requests.get('https://jsonplaceholder.typicode.com'
                f'/users/{id}/todos/')
        tasks = resp_task.json()
        all_user_dict[id] = [
                {
                    "username": user.get("username"),
                    "task": task.get("title"),
                    "completed": task.get("completed")
                    } for task in tasks
                ]
    with open('todo_all_employees.json', 'w') as file:
        json.dump(all_user_dict, file)
