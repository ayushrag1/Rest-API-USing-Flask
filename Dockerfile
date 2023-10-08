# Use the official Python image as the base image
FROM python:3.10.12-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the application files to the container
COPY . /app

# Install any necessary dependencies
RUN pip install -r requirements.txt

# Expose the port that the Flask app will run on (you should update this if needed)
EXPOSE 5000

# Define the command to start the Flask app
CMD ["python", "app.py"]