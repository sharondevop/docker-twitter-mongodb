# Use an official Python runtime as a parent image
FROM python:3.6.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the app code file into the container at /app
COPY tweets-with-python-to-mongodb.py /app

# Copy requirements.txt file into the container at /opt
COPY requirements.txt /opt

# Install any needed packages specified in requirements.txt
RUN pip3 install --trusted-host pypi.python.org -r /opt/requirements.txt

# Define environment variable
# you could give ARG a default value as well
ARG CONSUMER_KEY 
ARG CONSUMER_SECRET
ARG ACCESS_TOKEN
ARG ACCESS_TOKEN_SECRET
ARG MONGO_HOST

ENV CONSUMER_KEY=${CONSUMER_KEY} \ 
        CONSUMER_SECRET=${CONSUMER_SECRET} \
        ACCESS_TOKEN=${ACCESS_TOKEN} \
        ACCESS_TOKEN_SECRET=${ACCESS_TOKEN_SECRET} \
        MONGO_HOST=${MONGO_HOST}

# Run app  when the container launches
CMD ["python", "tweets-with-python-to-mongodb.py"]
