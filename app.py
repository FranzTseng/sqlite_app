# import queries from queries.py
# import sqlite
from queries import *
import sqlite3

# create a menu
menu = """1) Add a new command
2) Add a label to the command
3) Display all commands
4) Search commands by labels
5) Search commands by keywords
6) Exit
Select operation: """


# create all tables
create_tables()


operation = input(menu)

# create operation functions
def prompt_new_label(command_id):
    labels = input("Enter the label for the commands(split with ','): ").split(",")
    for lab in labels:
        add_label(lab,command_id)
def display_commands(commands):
    for row in commands:
        print("")
        print(f"Type of language:{row[0]}")
        print(f"labels: {row[3]}")
        print("---------------------------------")
        print(f"{row[1]}")
        print("--  --  --  --  --  --  -- --  --")
        print(f"{row[2]}") 
        print("---------------------------------")
        print("\n\n") 



# menu selections
while operation != "6":
    if operation=="1":
        lan = input("Which language: ")
        com = input("Command: ")
        des = input("Enter command decription: ")
        # fill in commands table
        add_command(lan, com, des) 
        # fill in labels table
        labels = input("Enter label(split with ','): ").split(",")
        add_label(labels)
        # fill in match table
        command_id = get_command_id(com)
        label_ids = get_label_id(labels)
        for label_id in label_ids:
            add_matching(command_id, label_id)
    elif operation=="2":
        pass
    elif operation=="3":
        commands = show_commands()
        display_commands(commands)
    elif operation=="4":
        pass
    elif operation=="5":
        pass
    operation = input(menu)

