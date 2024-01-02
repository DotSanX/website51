import sqlite3

conn = sqlite3.connect('db.sqlite')
cur = conn.cursor()

# тут пишите запросы через cur.execute("""запрос""")
cur.execute(""" CREATE TABLE IF NOT EXISTS posts
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    image TEXT DEFAULT NULL,
    title TEXT DEFAULT NULL,
    content TEXT DEFAULT NULL
 );""")   
conn.close()