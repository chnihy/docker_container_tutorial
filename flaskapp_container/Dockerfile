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