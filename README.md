# Simple Flask App

1. Create a simple Python web application using Flask.
2. Create a database with SQLite3
3. Modify the code to interact via SQLAlchemy.
4. Containerize it with Docker

## Notes

Flask supports Python 3.8 and newer.

```bash
python3 --version
```

### Virtual environments
Use a virtual environment to manage the dependencies for your project, both in development and in production.

Virtual environments are independent groups of Python libraries, one for each project. Packages installed for one project will not affect other projects or the operating system’s packages.

Python comes bundled with the venv module to create virtual environments.

Create and activate an environment:

```bash
python3 -m venv .venv
. .venv/bin/activate
```

### Install Flask

```bash
pip install --upgrade pip
pip install Flask
```

### Minimal Application

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```

### Run

```bash
flask run
```

Default port is 5000. Go to http://127.0.0.1:5000/

### If you need pick a different port
```bash
flask run --port 5001
```

### Add a database with SQLite3
```bash
python3 init-db.py
```

```python
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
```

### Run 
```bash
python3 app.py
```

### Query the database
```bash
sqlite3 site.db
.schema
SELECT * FROM technologies;
```

### Use SQLAlchemy
- With this approach we don't need the init-db.py script.
- Delete the site.db file.
- Run ```python3 app.py```

### Containerize it with Docker
Create the Dockerfile with the configuration 
```Dockerfile
# Use a Python base image
FROM python:3.10

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies defined in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5001 (in MacOS, AirPlay uses ports 5000 and 7000!)
EXPOSE 6000

# Default command to run your application when the container starts
CMD ["python", "app.py"]
```

Create the image
```bash
docker build -t simple-flask-app .
```

And run the container
```bash
docker run -p 5001:5001 simple-flask-app
```

### Use docker-compose 
```bash
docker-compose up
docker-compose down
```