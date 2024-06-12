import sqlite3

conn = sqlite3.connect('library.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS memberships (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        membership_number TEXT NOT NULL,
        duration INTEGER NOT NULL,
        status TEXT NOT NULL DEFAULT 'active'
    )
''')

conn.commit()
conn.close()
