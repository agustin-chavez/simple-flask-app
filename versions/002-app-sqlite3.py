from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


# Render the technologies in the template after executing init-db.py
@app.route('/')
def home():
    connection = sqlite3.connect('site.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM technologies')
    technologies = cursor.fetchall()
    connection.close()
    print(technologies)
    return render_template('index.html', technologies=technologies)

if __name__ == '__main__':
    app.run(debug=True)
