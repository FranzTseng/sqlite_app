## Introduction
This application is designed to store commands that I encountered throughout my learning journy. It can categorize data by different languages and store them in a sqlite database.

## Functionalities
 - **Input data:** Once choose insert data in the menu, new learned command could be put into the database by languages. The application would ask to enter labels for this piece of data. 
 - **Show data:** When this is chosen in the menu, all data in the sqlite database will be shown without labels attached to them.
 - **Search:** Data can be searched by languages and by labels.

## Database structure
 - **commands table:** This table stores commands learned and its descriptions.
 - **labels table:** This table stores all labels entered in the past and could be retrieved to provide a multiple choices menu for the user to choose from when they try to enter new labels for a new command.
 - **matched table:** This table connect the commands id in command table and the label id in labels table.

## Files
 - **app.py:** This is the main apllication python file to run.
 - **queries.py:** This file contains SQL queries and python codes to interact with sqlite database.
