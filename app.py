from flask import Flask, render_template, request, url_for, flash, redirect
# render_template - for html
import sqlite3
from werkzeug.exceptions import abort

def get_db_connection():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    return connection


def get_post(post_id):
    connection = get_db_connection()
    post = connection.execute('SELECT * FROM posts WHERE id = ?',
            (post_id,)).fetchone()
    connection.close()
    if post is None:
        abort(404)
    return post

app = Flask(__name__)
apps.config['SECRET_KEY'] = 'secret_key'
"""
Функция flash( from flask import flash ) хранит всплывающие сообщения в сеансе браузера клиента, что требует настройки секретного ключа. Этот секретный ключ используется для защищенных сеансов, что позволяет Flask запоминать информацию от одного запроса к другому, например, переходить от страницы нового поста к странице индекса. Пользователь может получить доступ к информации, хранящейся в сеансе, но не может изменить ее без секретного ключа. Поэтому никогда никому не передавайте доступ к вашему секретному ключу.
"""

@app.route('/')
def index():
    connection = get_db_connection()
    posts = connection.execute('SELECT * FROM posts').fetchall()
    connection.close()
    return render_template('index.html', posts=posts)


@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)


@app.route('/create', methods=('GET', 'POST'))
def create():
    return render_template('create.html')


if __name__ == '__main__':
    app.run(debug=True,port=8080)

