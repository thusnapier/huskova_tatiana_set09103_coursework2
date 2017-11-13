import sqlite3

with sqlite3.connect("texts.db") as connection:
  c = connection.cursor()
  c.execute("CREATE TABLE posts(auth TEXT, stat TEXT)")
  c.execute('INSERT INTO posts VALUES("Eva", "I get ignored")')
  c.execute('INSERT INTO posts VALUES("Adam", "my english teecher is a racist")')

