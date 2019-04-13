# Use an official Python runtime as a parent image
FROM python:3.6-slim

# Set the working directory to /app
WORKDIR /app

# copy project
COPY . /app

# Get pip to download and install requirements:
RUN pip install -r requirements.txt
 
# copy entrypoint.sh
COPY ./entrypoint.sh /app/entrypoint.sh

# copy project
COPY . /app

# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
