import sqlite3

with sqlite3.connect("texts.db") as connection:
  c = connection.cursor()
  c.execute("DROP TABLE IF EXISTS posts")
  c.execute("CREATE TABLE posts(auth TEXT not null, stat TEXT not null)")
  c.execute('INSERT INTO posts VALUES("Eva", "I get ignored")')
  c.execute('INSERT INTO posts VALUES("Adam", "my english teecher is a racist")')

with sqlite3.connect("users.db") as connection:
  c = connection.cursor()
  c.execute("DROP TABLE IF EXISTS user")
  c.execute("CREATE TABLE user(username TEXT not null, password TEXT not null)")
  c.execute('INSERT INTO user VALUES("Jack", "jackie")')
  c.execute('INSERT INTO user VALUES("Emily", "emms")')
