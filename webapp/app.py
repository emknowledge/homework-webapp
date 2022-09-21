import sqlite3
from flask import Flask, render_template

def get_db_connection():
    conn = sqlite3.connect('database.db')
    #name-based access to columns. This means that the database connection will return rows
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    # object as an argument, which contains the results you got from the database, 
    # this will allow you to access the posts in the index.html template.
    return render_template('index.html', posts=posts)

if __name__ =='__main__':
    app.run(port=1337 ,debug=True)