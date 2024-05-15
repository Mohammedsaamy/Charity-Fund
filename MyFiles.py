import json

# For users
users = {}
USERS_FILE = "users.json"


def save_to_file_from_user(file_name, data):
    with open(file_name, "w") as file:
        json.dump(data, file)


def load_from_file(file_name):
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        
        return []


# for project
projects = []
PROJECTS_FILE = "projects.json"
def save_to_file_from_project(file_name, data):
    existing_data = load_from_file(file_name)
    existing_data.extend(data)

    with open(file_name, "w") as file:
        json.dump(existing_data, file)