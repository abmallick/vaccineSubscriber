import sqlite3

connection = sqlite3.connect('database.db')


with open('utilities/request_schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.executemany("INSERT INTO requests (pin_code, email_id) VALUES (?,?)",
                [(160104, 'abc@gmail.com'),
                 (800014, 'xyz@gmail.com')]
                )

connection.commit()
connection.close()
