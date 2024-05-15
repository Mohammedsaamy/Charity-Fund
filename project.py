from MyFiles import *
import re


import datetime

def date_form(time):
    try:
        datetime.date.fromisoformat(time)
    except ValueError:
        print("Date format isn't correct")
        return False
    else:
        return True



# *********************************************************************
# Create 
    

def create_project(user_email):
    print("-------------Create New Project--------------")
    title = input("Please enter The Title : ")
    details = input("Please enter The Details : ")

    total_target = input("Please enter project target : ")

    while not total_target.isdigit():
        print("target should be numeric values!!")
        total_target = input("Please enter correct project target : ")

    start_time = input("Please enter project start time in this form yyyy-mm-dd: ")
    while not date_form(start_time):
        start_time = input("Please enter project start time in this form yyyy-mm-dd: ")
    end_time = input("Please enter project end time in this form yyyy-mm-dd: ")
    while not date_form(end_time):
        end_time = input("Please enter project end time like in this form yyyy-mm-dd: ")

    project = {
        "user_email": user_email,
        "title": title,
        "details": details,
        "total target(EGY)": total_target,
        "start_time": start_time,
        "end_time": end_time
    }
    projects.append(project)
    save_to_file_from_project(PROJECTS_FILE, [project])

    print("Project created successfully")


# *********************************************************************


# Delete 
    
def delete_project(user_email):
    print("------------Delete Project------------")
    title = input("Please enter the title of the project  to Delete: ")

    for project in projects:
        if project["user_email"] == user_email and project["title"] == title:
            projects.remove(project)
            save_to_file_from_project(PROJECTS_FILE, [project])
            print("Project deleted successfully")
            print("----------------------------")
            
    print("Project not found")
    print("----------------------------")

# *********************************************************************

# Edit
    
def edit_project(user_email):
    print("------------Edit Project------------")
    title = input(" Please enter the title of the project that you want to edit: ")

    for project in projects:
        if project["user_email"] == user_email and project["title"] == title:
            print(" ---------------Now you Can Edit the project---------------")

            # Edit project details
            while True:
                print("Which detail do you want to edit?")
                print("1. Title")
                print("2. Details")
                print("3. Total target")
                print("4. Start time")
                print("5. End time")
                print("6. Exit")

                choice = input("Please Enter your choice: ")

                if choice == '1':
                    project["title"] = input("New title: ")
                elif choice == '2':
                    project["details"] = input("New details: ")
                elif choice == '3':
                    project["total_target"] = input("New total target: ")
                elif choice == '4':
                    project["start_time"] = input("New start time (yyyy-mm-dd): ")
                elif choice == '5':
                    project["end_time"] = input("New end time (yyyy-mm-dd): ")
                elif choice == '6':
                    break
                else:
                    print("Invalid choice. Please try again.")

            save_to_file_from_project(PROJECTS_FILE, [project])
            print("Project edited successfully")
            print("----------------------------")
            return

    print("Project not found")
    print("----------------------------")


# *********************************************************************

# Search


    
def search_projects(user_email):
    print("------------Search Projects ------------")

    # Search projects
    title = input("Please enter the title of the project that you want to Search: ")
    for project in projects:
        if project["user_email"] == user_email and project["title"] == title :
            print("----------------------------")
            print(f"Title: {project['title']}")
            print(f"Details: {project['details']}")
            print(f"Total target: {project['total target(EGY)']}")
            print(f"Start time: {project['start_time']}")
            print(f"End time: {project['end_time']}")
            break

        else:
            print("No projects to show.")
            print("----------------------------")



# *********************************************************************

# View


def view_projects(user_email):
    print("------------viewing projects--------------")
    for project in projects:
        if project["user_email"] == user_email:
            print(f"Title: {project['title']}")
            print(f"Details: {project['details']}")
            print(f"Total target: {project['total target(EGY)']}")
            print(f"Start time: {project['start_time']}")
            print(f"End time: {project['end_time']}")
            print("----------------------------")


        else:
            print("No projects to show.")
            print("----------------------------")


# *********************************************************************

# Login


def login():
    print("--------------------Login--------------------")
    attempts = 3

    while attempts > 0:
        email = input("Please Enter your email: ")
        password = input("Please Enter your password: ")

        user = users.get(email)
        if user and user["password"] == password:
            print("Success login")
            print("------------welcome to our system--------------------")
            return user["email"]

        print(f"Invalid email or password. {attempts - 1} attempts left.")
        attempts -= 1

    print("you used all your login attempts.")
    print("--------------------------------")



# *********************************************************************

# Register
    

def register():
    print("------Registration------")

    first_name = input(" Please Enter your First name: ")
    while not first_name.isalpha():
        print('---------------Invalid name-----------------')
        first_name = input("Please enter your first name again: ")

    last_name = input(" Please Enter your Last name: ")
    while not last_name.isalpha():
        print('---------------Invalid name-----------------')
        last_name = input("Please enter your last name again: ")

    email = input("Please Enter your Email: ")
    if email in users:
        print("Email already exists.")
        print('--------------------------------')
        return
    while not re.match("^[a-zA-Z0-9-_.]+@[a-zA-Z0-9]+\.[a-z]{1,3}$", email):
        print("---------------Invalid email address-----------------")
        email = input("Please Enter your Email: ")

    password = input("Please Enter your Password: ")
    confirm_password = input("Confirm your password: ")
    while password != confirm_password:
        print("Passwords don't match")
        print('--------------------------------')
        password = input("Please Enter your Password again: ")
        confirm_password = input(" Please Confirm your password")

    phone_number = input("Please Enter your phone number: ")
    phone_pattern = "^(\+201|01|00201)[0-2,5]{1}[0-9]{8}"
    while not re.match(phone_pattern, phone_number):
        print("Your phone does not match egyptian phone numbers")
        print('--------------------------------')
        phone_number = input("Please enter your phone number again: ")
    print("Valid phone number")

    users[email] = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "mobile_phone ": phone_number
    }
    save_to_file_from_user(USERS_FILE, users)

    print("Registration successful")
    print("--------------------------------")



# *********************************************************************

# Menu


def main():

    users.update(load_from_file(USERS_FILE))
    projects.extend(load_from_file(PROJECTS_FILE))
    while True:
        print("----------------Welcome To Crowd funding App------------ ")
        print("1. Register")
        print("2. Login")
        print("3. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            register()
        elif choice == "2":
            user_email = login()

            if user_email:
                while True:
                    print("1. Create Project")
                    print("2. View Projects")
                    print("3. Edit Project")
                    print("4. Delete Project")
                    print("5. Search Projects")
                    print("6. Log out")

                    inner_choice = input("Choose an option: ")
                    if inner_choice == "1":
                        create_project(user_email)
                    elif inner_choice == "2":
                        view_projects(user_email)
                    elif inner_choice == "3":
                        edit_project(user_email)
                    elif inner_choice == "4":
                        delete_project(user_email)
                    elif inner_choice == "5":
                        search_projects(user_email)
                    elif inner_choice == "6":
                        break


        elif choice == "3":
            print("Thank You For Your Time, Until We See You Again")
            break
        else:
            print("please enter vaild choice (1 or 2 or 3) ")