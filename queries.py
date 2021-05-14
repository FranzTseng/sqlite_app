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
            label TEXT,
            command_id INTEGER,
            FOREIGN KEY(command_id) REFERENCES commands(id)
);"""


# insert new command
INSERT_COMMAND = """INSERT INTO commands (language, command, description) 
                    VALUES (?,?,?);"""
INSERT_LABEL = "INSERT INTO labels (label,command_id) VALUES (?,?);"
SHOW_COMMANDS = """SELECT language, command, description, label
                   FROM commands
                   JOIN labels 
                   ON labels.command_id = commands.id;"""
GET_COMMAND_ID = "SELECT id FROM commands WHERE command=?;"

# establish connection
conn = sqlite3.connect("data.db")


# define functions
def create_tables():
    with conn:
        conn.execute(CREATE_COMMAND_TABLE)
        conn.execute(CREATE_LABEL_TABLE)

def add_command(lan, com,des):
    with conn:
        cursor = conn.cursor()
        cursor.execute(INSERT_COMMAND,(lan, com, des))
def add_label(lab,command_id):
    with conn:
        cursor = conn.cursor()
        cursor.execute(INSERT_LABEL, (lab,command_id))
def show_commands():
    with conn:
        cursor = conn.cursor()
        cursor.execute(SHOW_COMMANDS)
        return cursor.fetchall()
def get_id(com):
    with conn:
        cursor = conn.cursor()
        cursor.execute(GET_COMMAND_ID,(com,))
        return cursor.fetchone()[0]
