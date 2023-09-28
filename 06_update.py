import sqlite3
import os

connection = sqlite3.connect("data/contacts.db")

cursor = connection.cursor()

# update the database to add annie Oakley email:anna@mit.edu
cursor.execute("""INSERT INTO contacts
    VALUES 
    ('annie', 'Oakley', 'anna@mit.edu')""")

# verify that the row was added
rows = cursor.execute("SELECT * FROM contacts")
print(rows.fetchall())

# update the database to change peter's name to Peter

cursor.execute(
    "UPDATE contacts SET firstname = 'Peter' WHERE firstname = 'peter'")
connection.commit()
