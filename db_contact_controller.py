import sqlite3

conn = sqlite3.connect('db.sqlite')
cur = conn.cursor()

# поправил типы None на Null (Максим)
cur.execute(""" CREATE TABLE IF NOT EXISTS contacts
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT DEFAULT NULL,
    description TEXT DEFAULT 'У этого чувака нет истории... есть только путь...',
    color TEXT DEFAULT '#ffffff',
    image TEXT DEFAULT '/static/image/contacts_anonimus.jpg',
    username TEXT,
    password TEXT,
    url_youtube TEXT DEFAULT NULL,
    url_telegram TEXT DEFAULT NULL,
    url_vk TEXT DEFAULT NULL,
    url_instagram TEXT DEFAULT NULL,
    url_discord TEXT DEFAULT NULL
);""")

cur.execute("""select * from contacts;""")
print(cur.fetchall())

conn.close()
