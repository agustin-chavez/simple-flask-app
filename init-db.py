import sqlite3

# Create a simple database to store technologies
connection = sqlite3.connect('site.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS technologies (id INTEGER PRIMARY KEY, name TEXT NOT NULL)')
for technology in ['Python', 'SQLite3', 'Flask', "Docker" ]:
    cursor.execute('INSERT INTO technologies (name) VALUES (?)', (technology, ))
connection.commit()
connection.close()