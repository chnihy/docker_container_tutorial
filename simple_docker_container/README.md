# SIMPLE DOCKER CONTAINER TUTORIAL

## Project Structure

```
.
├── Dockerfile
└── main.py
```
## 1. Download and install Docker Desktop

## 2. Create your main.py file

```bash
touch main.py
open main.py
```

<p class="codeblock-label">main.py</p>

```python
import requests
"""
All of this code is arbitrary for the sake of this tutorial.
It is only used to demonstrate a script that requires
a third party package ('requests')
"""


# sending a get request
request = requests.get("https://www.google.com/")

# printing request info that is returned
print("Status Code: {}".format(request.status_code))
print("URL: {}".format(request.url))
print("Request: {}".format(request.request))
```


## 3. Create your Dockerfile

```bash
touch Dockerfile
open Dockerfile
```

<p class="codeblock-title">Dockerfile</p>

```Dockerfile
# Start with a pre-made image
FROM python:3.8

# Add main file (main.py) to current container (.)
ADD main.py .

# Install requirements
RUN pip install requests

# Entry command for start of container
CMD [ "python3", "./main.py" ]
```

## 4. Build Docker image

```bash
$ docker build -t myapp .
```

## 5. Run application
```bash
docker run myapp
```
