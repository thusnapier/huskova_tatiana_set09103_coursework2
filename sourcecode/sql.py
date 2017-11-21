import sqlite3
import bcrypt

with sqlite3.connect("texts.db") as connection:
  c = connection.cursor()
  c.execute("DROP TABLE IF EXISTS posts")
  c.execute("CREATE TABLE posts(auth TEXT not null, stat TEXT not null)")
  c.execute('INSERT INTO posts VALUES("Emily", "Hello there from Napier")')
  c.execute('INSERT INTO posts VALUES("Jack", "Im trying to make my code work")')
  c.execute('INSERT INTO posts VALUES("Scott", "Its a terrible weather")')
  c.execute('INSERT INTO posts VALUES("Olivia", "Ive never heen happier!!!")')

with sqlite3.connect("users.db") as connection:
  c = connection.cursor()
  c.execute("DROP TABLE IF EXISTS user")
  c.execute("CREATE TABLE user(username TEXT not null, password TEXT not null)")
  hashed = bcrypt.hashpw("jackie", bcrypt.gensalt(12))
  c.execute('INSERT INTO user VALUES("Jack","' +hashed+ '")')
  hashed = bcrypt.hashpw("emms", bcrypt.gensalt(12))
  c.execute('INSERT INTO user VALUES("Emily", "' +hashed+ '")')
  hashed = bcrypt.hashpw("scotty", bcrypt.gensalt(12))
  c.execute('INSERT INTO user VALUES("Scott", "' +hashed+ '")')
  hashed = bcrypt.hashpw("liv", bcrypt.gensalt(12))
  c.execute('INSERT INTO user VALUES("Olivia", "' +hashed+ '")')
