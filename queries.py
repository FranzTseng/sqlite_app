# import libraries
import sqlite3

# create tables
CREATE_COMMAND_TABLE = """CREATE TABLE IF NOT EXIST commands (
            id INTEGER PRIMARY KEY,
            language TEXT,
            command TEXT,
            description TEXT
);"""

CREATE_LABEL_TABLE =  """CREATE TABLE IF NOT EXISTS labels (
            id INTEGER,
            label TEXT
);"""

CREATE_LABEL_MATCH_TABLE = """CREATE TABLE IF NOT EXISTS match (
            command_id INTEGER,
            label_id INTEGER,
            FOREIGN KEY(command_id) REFERNECES commands(id),
            FOREIGN KEY(label_id) REFERENCES labels(id)
);"""

# insert new command
INSERT_COMMAND = """INSERT INTO commands (language, command, description) 
                    VALUES (?,?,?);"""
INSERT_LABEL = "INSERT INTO labels (label) VALUES (?);"
INSERT_MATCHING = """INSERT INTO match (command_id, label_id)
                     VALUES (?,?);"""
SHOW_COMMANDS = """SELECT * FROM commands
                   JOIN match ON commands.id = match.command_id
                   JOIN labels ON match.label_id = labels.id;"""




