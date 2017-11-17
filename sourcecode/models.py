import sqlite3 as sql

def getUser(username, password):
  con = sql.connect("users.db")
  cur  = con.cursor()
  cur.execute("SELECT password FROM user WHERE username ='"+username+"'") 
  user = cur.fetchone()
  con.close()
  if password == user[0]:
   return True
  else:
   return False

def sharePost(auth, stat):
  con = sql.connect("texts.db")
  cur = con.cursor()
  cur.execute("INSERT INTO posts (auth, stat) VALUES(?,?)",(auth, stat))
  con.commit()
  con.close()

def getPost():
  con = sql.connect("texts.db")
  cur = con.cursor()
  cur.execute("SELECT auth, stat FROM posts")
  posts = cur.fetchall()
  con.close()
  return posts

