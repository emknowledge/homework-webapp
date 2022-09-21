import sqlite3
#connection to a database file named database.db, 
#which will be created once you run the Python file.
connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    # method that executes multiple SQL statements at once, which will create the posts table.
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title) VALUES (?)",
            ['First Post']
            )

cur.execute("INSERT INTO posts (title) VALUES (?)",
            ['Second Post']
            )

connection.commit()
connection.close()
