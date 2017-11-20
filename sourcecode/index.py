from flask import Flask, render_template, request, redirect, url_for, session, flash, g
from functools import wraps
import sqlite3
import models as dbHandler
import bcrypt

app = Flask(__name__)

app.secret_key = "simon"
app.database1 = "texts.db"
app.database2 = "users.db"

valid_username = 'username'
valid_pwhash = bcrypt.hashpw('secretpass', bcrypt.gensalt())

#def check_auth(form):
#  if(valid_pwhash ==
#  bcrypt.hashpw(form[1].encode('utf-8'), valid_pwhash)):
#    return True
#  return False

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

@app.route('/welcome', methods=['GET','POST'])
@login_required
def welcome():
  if request.method == 'POST':
    g.db = connect_dab()
    cur = g.db.execute('SELECT auth, stat FROM posts')
    posts = [dict(auth=row[0], stat=row[1]) for row in cur.fetchall()]
    text = request.form['text']
    insname = request.form['insname']
    inserted_name = insname
    processed_text = text
    inserted_text=dbHandler.sharePost(insname,text)
    g.db.close()
    return render_template('logedin.html',inserted_name=inserted_name,
    processed_text=processed_text, insname=insname, text=text, posts=posts)
  else:
    session['logged_in']=True
    g.db = connect_dab()
    cur = g.db.execute('SELECT auth, stat FROM posts')
    posts = [dict(auth=row[0], stat=row[1]) for row in cur.fetchall()] 
    g.db.close()
    return render_template('logedin.html', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
#@check_auth
def login():
  error = None
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    user = dbHandler.getUser(username, password)
    if user==True:
      session['logged_in'] = True
      return redirect(url_for('welcome'))
    else:
      session['logged_in'] = False
      flash('Incorrect login details!')
      return render_template('login.html')
  else:
    session['logged_in'] = True 
    return render_template('login.html')
     
@app.route('/logout')
@login_required
def logout():
  session.pop('logged_in', None)
  flash('You were logged out from the page.')
  return redirect(url_for('homepage'))

def connect_db():
  return sqlite3.connect(app.database2)

def connect_dab():
  return sqlite3.connect(app.database1)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
