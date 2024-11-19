import sys

# Initialize an empty to-do list

todo_list = []

# Function to display the to-do list

def display_todo_list():
if not todo_list:
print("\nYour to-do list is empty!\n")
@@ -14,13 +14,13 @@ def display_todo_list():
print(f"{i}. {task['task']} - {status}")
print()

# Function to add a new task
# now we add a new task
def add_task():
task_name = input("Enter the task: ")
todo_list.append({'task': task_name, 'completed': False})
print(f"Task '{task_name}' added to your to-do list!\n")

# Function to update a task
# now we can update a task
def update_task():
display_todo_list()
if not todo_list:
@@ -36,7 +36,7 @@ def update_task():
except ValueError:
print("Please enter a valid number!\n")

# Function to delete a task
# we can enable the  delete option may be after completion a task
def delete_task():
display_todo_list()
if not todo_list:
@@ -52,7 +52,7 @@ def delete_task():
except ValueError:
print("Please enter a valid number!\n")

# Function to display the menu
# function to display the menu
def display_menu():
print("To-Do List Menu:")
print("1. View To-Do List")
@@ -61,7 +61,7 @@ def display_menu():
print("4. Delete Task")
print("5. Exit")

# Main loop for the application

def main():
print("Welcome to the To-Do List Application!")  # Added welcome message
while True:
@@ -82,6 +82,6 @@ def main():
else:
print("Invalid choice! Please select an option between 1 and 5.\n")

# Entry point for the script

if __name__ == "__main__":
    main()  # Make sure the main function is called
    main() 