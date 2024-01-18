# Use an official Python runtime as a parent image
FROM python:3.11.7

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
# (replace "requirements.txt" with the actual name of your requirements file)
RUN pip install -r requirements.txt

# Make port 3000 available to the world outside this container
EXPOSE 8080

# Define environment variable
# ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
