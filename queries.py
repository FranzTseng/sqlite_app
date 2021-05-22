# import libraries
import sqlite3

# create tables
CREATE_COMMAND_TABLE = """CREATE TABLE IF NOT EXISTS commands (
            id INTEGER PRIMARY KEY,
            language TEXT,
            command TEXT,
            description TEXT
);"""

CREATE_LABEL_TABLE =  """CREATE TABLE IF NOT EXISTS labels (
            id INTEGER PRIMARY KEY,
            label TEXT
);"""

CREATE_MATCH_TABLE = """CREATE TABLE IF NOT EXISTS match (
            command_id,
            label_id,
            FOREIGN KEY(command_id) REFERENCES commands(id),
            FOREIGN KEY(label_id) REFERENCES labels(id)
);"""

# queries 
INSERT_COMMAND = """INSERT INTO commands (language, command, description) 
                    VALUES (?,?,?);"""
INSERT_LABEL = "INSERT INTO labels (label) VALUES (?);"
INSERT_MATCHING = "INSERT INTO match (command_id, label_id) VALUES (?,?);"
SHOW_COMMANDS = "SELECT * FROM commands;"
SELECT_CURRENT_LABELS = """SELECT * FROM labels;"""
GET_COMMAND_ID = "SELECT id FROM commands WHERE command=?;"
GET_LABEL_ID = "SELECT id FROM labels WHERE label=?;"

# establish connection
conn = sqlite3.connect("data.db")


# define a function to create tables
def create_tables():
    with conn:
        conn.execute(CREATE_COMMAND_TABLE)
        conn.execute(CREATE_LABEL_TABLE)
        conn.execute(CREATE_MATCH_TABLE)

# define a function for the commands table
def add_command(lan, com,des):
    with conn:
        cursor = conn.cursor()
        cursor.execute(INSERT_COMMAND,(lan, com, des))

# define functions for labels table 
# print labels choices menu
def print_label_menu():
    with conn:
        cursor = conn.cursor()
        # grab all current labels in labels table
        result = cursor.execute(SELECT_CURRENT_LABELS).fetchall()
        # add "Others" choice at the end of the tuple list
    if result != []:
        result.insert(len(result), ((result[-1][0]+1),"Others"))
        label_menu = dict(result)
    else: 
        result.insert(0, (1, "Others"))
        print("No label in the database, please choose 'others'")
        label_menu = dict(result)
    for k, i in result:
        print(f"{k}) {i}")
    
    return dict(result)
# define function to add a label into the table
# define a function to take multiple labels input and parse them to add_label function
def add_label(*args):
    with conn:
        cursor = conn.cursor()
        for arg in args:
#            if arg != "":
            cursor.execute(INSERT_LABEL, (arg,))
# define functions for matching table        
def add_matching(command_id,label_id):
    with conn:
        cursor = conn.cursor()
        cursor.execute(INSERT_MATCHING,(command_id, label_id))
def get_command_id(com):
    with conn:
        cursor = conn.cursor()
        cursor.execute(GET_COMMAND_ID,(com,))
        com_id = cursor.fetchone()[0]
        return com_id
def get_label_id(labs):
    with conn:
        cursor = conn.cursor()
        lab_ids=[]
        for lab in labs:
            cursor.execute(GET_LABEL_ID, (lab,))
            lab_id = cursor.fetchone()[0]
            lab_ids.append(lab_id)
    return lab_ids

# define function to show all the data
def show_commands():
    with conn:
        cursor = conn.cursor()
        cursor.execute(SHOW_COMMANDS)
        return cursor.fetchall()
