import sqlite3
import os

connection = sqlite3.connect("data/contacts.db")

cursor = connection.cursor()

# read from the database
rows = cursor.execute("SELECT * FROM contacts")
print(rows.fetchall())
