from flask import Flask, render_template, request, redirect, url_for, session, flash, g
from functools import wraps
import sqlite3

app = Flask(__name__)

app.secret_key = "simon"
app.database = "texts.db"

#decorator that requires login before seeing the content
def login_required(f):
  @wraps(f)
  def wrap(*args,**kwargs):
    if 'logged_in' in session:
      return f(*args, **kwargs)
    else:
      flash('Log in to see the content.')
      return redirect(url_for('login'))
  return wrap

@app.route('/')
def homepage():
  return render_template('base.html')

@app.route('/welcome')
@login_required
def welcome():
# g.db = connect_db()
# cur = g.db.execute('SELECT * FROM posts')
# posts = [dict(auth=row[0], stat=row[1]) for row in cur.fetchall()]
# g.db.close()
  return render_template('logedin.html')

@app.route('/welcome', methods=['POST'])
def welcome_post():
  text = request.form['text']
  processed_text = text
  return render_template('logedin.html', processed_text=processed_text)


@app.route('/login', methods=['GET', 'POST'])
def login():
  error = None
  if request.method == 'POST':
    if request.form['username'] != 'cscott' or request.form['password'] != 'scotty':
      error = 'Invalid login details. Please try again.'
    else:
      session['logged_in'] = True
      flash('You were successfully logged in!') 
      return redirect(url_for('welcome'))
  return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
  session.pop('logged_in', None)
  flash('You were logged out from the page.')
  return redirect(url_for('homepage'))

def connect_db():
  return sqlite3.connect(app.database)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
