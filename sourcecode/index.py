from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps

app = Flask(__name__)

app.secret_key = "simon"

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
  return render_template('logedin.html')

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
  flash('You were logged out from the pgae.')
  return redirect(url_for('homepage'))

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
