import sqlite3 as sql
import bcrypt

#get users from the database
def getUser(username, password):
  con = sql.connect("users.db")
  cur  = con.cursor()
  cur.execute("SELECT password FROM user WHERE username ='"+username+"'") 
  user = cur.fetchone()
  con.close()
  hashed = user[0]
  password.encode('utf-8')
  #if password == user[0]:
  if bcrypt.checkpw(password, hashed):
   return True
  else:
   return False

#share post and send it itno the database
def sharePost(auth, stat):
  con = sql.connect("texts.db")
  cur = con.cursor()
  cur.execute("INSERT INTO posts (auth, stat) VALUES(?,?)",(auth, stat))
  con.commit()
  con.close()

#get posts from the database
def getPost():
  con = sql.connect("texts.db")
  cur = con.cursor()
  cur.execute("SELECT auth, stat FROM posts")
  posts = cur.fetchall()
  con.close()
  return posts

