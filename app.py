# import queries from queries.py
# import sqlite
from queries import *
import sqlite3

# create a menu
menu = """1) Add a new command
2) Display all commands
3) Search commands by keywords
4) Search commands by labels
5) Exit
Select operation: """


# create all tables
create_tables()



# create operation functions
def display_commands(commands):
    for row in commands:
        print("")
        print(f"Type of language: \033[91m{row[1]}\033[0m")
        print("---------------------------------")
        print(f"{row[0]}. \033[93m{row[2]}\033[0m")
        print("--  --  --  --  --  --  -- --  --")
        print(f"{row[3]}")
        print("---------------------------------")
        print("") 



# menu selections
operation = input(menu)
while operation != "6":
    if operation=="1":
        lan = input("Which language: ")
        com = input("Command: ")
        des = input("Enter command decription: ")
        # fill in commands table
        add_command(lan, com, des) 
        # fill in labels table
        label_list = print_label_menu()
        label_ids = input(f"Enter your labels(seperate with ','): ").split(",")
        command_id = get_command_id(com)
        if str(len(label_list)) in label_ids:
            labs = input(f"Enter new labels(seperate with ','): ").split(",")
            add_label(*labs)
        # fill in match table
            new_label_ids= get_label_id(labs)
            for label_id in new_label_ids:
                add_matching(command_id, int(label_id))
        else:
            for label_id in label_ids:
                add_matching(command_id, int(label_id))
    elif operation=="2":
        all_commands = show_commands()
        display_commands(all_commands)

    elif operation=="3":
        keyword = input("Keyword: ")
        seach_result = search_keywords(keyword)
        display_commands(seach_result)

    elif operation=="4":
        pass
    elif operation=="5":
        pass
    operation = input(menu)

