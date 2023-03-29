# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster
# Set the working directory to /app
WORKDIR /app
# Copy the client code into the container at /app
COPY . /app


RUN pip install --upgrade pip
# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
# Run greeter_client.py when the container launches
CMD ["python", "user_auth_client.py"]