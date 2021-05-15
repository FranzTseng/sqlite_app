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

# insert new command
INSERT_COMMAND = """INSERT INTO commands (language, command, description) 
                    VALUES (?,?,?);"""
INSERT_LABEL = "INSERT INTO labels (label) VALUES (?);"
INSERT_MATCHING = "INSERT INTO match (command_id, label_id) VALUES (?,?);"
SHOW_COMMANDS = """SELECT language, command, description, label
                   FROM commands
                   JOIN labels 
                   ON labels.command_id = commands.id;"""
GET_COMMAND_ID = "SELECT id FROM commands WHERE command=?;"
GET_LABEL_ID = "SELECT id FROM labels WHERE label=?;"
# establish connection
conn = sqlite3.connect("data.db")


# define functions
def create_tables():
    with conn:
        conn.execute(CREATE_COMMAND_TABLE)
        conn.execute(CREATE_LABEL_TABLE)
        conn.execute(CREATE_MATCH_TABLE)

def add_command(lan, com,des):
    with conn:
        cursor = conn.cursor()
        cursor.execute(INSERT_COMMAND,(lan, com, des))
def add_label(labs):
    with conn:
        cursor = conn.execute("SELECT label FROM labels;")
        row = cursor.fetchone()
        current_labels = []
        while row:
            current_labels.append(row[0])
            row = cursor.fetchone()
        for lab in labs:
            if lab not in current_labels:
                cursor.execute(INSERT_LABEL, (lab,))
def add_matching(command_id,label_id):
    with conn:
        cursor = conn.cursor()
        cursor.execute(INSERT_MATCHING,(command_id, label_id))
def show_commands():
    with conn:
        cursor = conn.cursor()
        cursor.execute(SHOW_COMMANDS)
        return cursor.fetchall()
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
