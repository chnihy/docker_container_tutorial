# Docker Flask App Container Tutorial

## Project Structure

```
.
├── Dockerfile
├── README.md
├── app
│   ├── main.py
│   └── templates
│       ├── base.html
│       └── index.html
└── requirements.txt

```
## 1. Download and install Docker Desktop

## 2. Create your app folder and main.py file

```bash
mkdir app
cd app
touch main.py
open main.py
```

<p class="codeblock-label">main.py</p>

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

"""
You can also set port/host as Environment variables 
by using <$ export PORT=500> <$export HOST=0.0.0.0>
"""
if __name__ == "__main__":
	app.run(port = 5000, host = "0.0.0.0")
```

*Not shown: create templates folder and template html files


## 3. Create your Dockerfile

```bash
touch Dockerfile
open Dockerfile
```

<p class="codeblock-title">Dockerfile</p>

```Dockerfile
# start with a pre-made image
FROM python:3.8

# create a working directory
WORKDIR /flask_app

# copy requirements
COPY requirements.txt .

# install requirements on build
RUN pip install -r requirements.txt

# copy application folder
COPY ./app ./app

# Command to run when container launched
CMD [ "python3", "./app/main.py" ]
```

## 4. Build Docker image

```bash
$ docker build -t flaskapp_container .
```

## 5. Run application
You must specify the local port and docker port otherwise you will get an error
```bash
docker run -p 5000:5000 flaskapp_container
```
