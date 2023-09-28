import sqlite3
import os

if os.path.exists("data/contacts.db"):
    os.remove("data/contacts.db")
    
connection = sqlite3.connect("data/contacts.db")
cursor = connection.cursor()

rows = cursor.execute("""CREATE TABLE contacts (
    firstname,
    lastname,
    email)""")

#verify that the table was created
rows = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(rows.fetchall())

