import sqlite3
from flask import Flask, render_template
from werkzeug.exceptions import abort

def get_db_connection():
    conn = sqlite3.connect('database.db')
    #name-based access to columns. This means that the database connection will return rows
    conn.row_factory = sqlite3.Row
    return conn

#argument that determines what blog post to return
def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    #if no result in database
    if post is None:
        abort(404)
    return post

app = Flask(__name__)

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    # object as an argument, which contains the results you got from the database, 
    # this will allow you to access the posts in the index.html template.
    return render_template('index.html', posts=posts)

#view function to get the post associated with the given ID and store the result in the post variable, which is passed to post.html
@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)


if __name__ =='__main__':
    app.run(port=1337 ,debug=True)