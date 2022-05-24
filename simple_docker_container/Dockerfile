# Start with a pre-made image
FROM python:3.8

# Add main file (main.py) to current container (.)
ADD main.py .

# Install requirements when container is built
RUN pip install requests

# Entry command for start of container
CMD [ "python3", "./main.py" ]