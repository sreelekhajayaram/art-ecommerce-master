import sqlite3
con = sqlite3.connect('db.sqlite3')
cur = con.cursor()
cur.execute("SELECT id, app, name FROM django_migrations WHERE app='booking'")
rows = cur.fetchall()
for r in rows:
    print(r)
