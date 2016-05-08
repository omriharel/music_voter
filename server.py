import thread
import sys
import sqlite3

from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash

# configuration
DATABASE = '/tmp/music_voter.db'
SECRET_KEY = 'development key'
DEBUG = True
USERNAME = 'admin'
PASSWORD = 'admin'

app = Flask(__name__)
app.config.from_object(__name__)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


@app.route('/')
def show_songs():
    cur = g.db.execute('select title, link, votes from songs order by id desc')
    songs = [dict(title=row[0], link=row[1], votes=row[2]) for row in cur.fetchall()]
    return render_template('show_songs.html', songs=songs)


@app.route('/songs', methods=['POST'])
def post_songs():
    g.db.execute('insert into songs (title, link, votes) values (?, ?, ?)',
                 [request.form['title'], request.form['link'], 0])
    g.db.commit()
    flash('New song was added to be voted on')
    return redirect(url_for('show_songs'))


if __name__ == "__main__":
    app.run()
