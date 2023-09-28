import sqlite3
import os

connection = sqlite3.connect("data/contacts.db")

cursor = connection.cursor()

# write to the database
cursor.execute("""INSERT INTO contacts
    VALUES 
    ('peter', 'Parker', 'peter@mit.edu'),
    ('bruce', 'Wayne', 'bruce@mit.edu'),
    ('diana', 'Prince', 'diana@mit.edu')""")
connection.commit()

rows = cursor.execute("SELECT * FROM contacts")
print(rows.fetchall())
