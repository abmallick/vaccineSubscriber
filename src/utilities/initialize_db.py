import sqlite3

connection = sqlite3.connect('database.db')


with open('utilities/request_schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO requests (pin_code, email_id) VALUES (?, ?)",
            ('160104', 'rdxvvvvv@gmail.com')
            )
cur.execute("INSERT INTO requests (pin_code, email_id) VALUES (?, ?)",
            ('160104', 'utkarsh.sahay13@gmail.com')
            )

connection.commit()
connection.close()