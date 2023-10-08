# Rest-API-Using-Flask
Takes data from base url and filter the data of base url based on given parameter that have passed on api calling


## Prerequisites

- Python 3.10.12
- Docker installed (if you plan to use Docker)
- Git installed (optional for version control)


# Setting up Python Virtual Environment for Running Flask App

This guide will walk you through the process of setting up a Python virtual environment to run a Flask application. A virtual environment allows you to isolate dependencies for your Flask app, ensuring a clean and consistent environment.

## Prerequisites

Before you proceed with the setup, make sure you have the following installed on your machine:

- Python: [Install Python](https://www.python.org/downloads/)

## Step 1: Clone the Repository

Clone the repository containing your Flask application code:

```
[git clone <https://github.com/ayushrag1/Sentence-Similarity-Score-Using-NLP.git>](https://github.com/ayushrag1/Rest-API-USing-Flask.git)
cd <Rest-API-USing-Flask>
```

## Step 2: Create a Virtual Environment

Create a new Python virtual environment for your Flask app:

### On Windows:

```
python -m venv venv
```

### On macOS and Linux:

```
python3 -m venv venv
```

This will create a new directory named `venv` that contains the virtual environment.

## Step 3: Activate the Virtual Environment

Activate the virtual environment to start using it:

### On Windows (cmd):

```
venv\Scripts\activate
```

### On Windows (PowerShell):

```
venv\Scripts\Activate.ps1
```

### On macOS and Linux:

```
source venv/bin/activate
```

## Step 4: Install Flask and Dependencies

With the virtual environment activated, you can now install Flask and other dependencies required for your application:

```
pip install -r requirements.txt
```

## Step 5: Run the Flask App

You are all set to run your Flask app now! Use the following command to start the development server:

```
python app.py
```

Your Flask app should now be accessible at `http://localhost:5000` in your web browser.
```
http://127.0.0.1:5000/search?search_author=Fredrick&search_text=economic&at_from=01-01-2023&at_to=01-02-2023&like_from=0&like_to=5&reply_from=0&reply_to=5
http://127.0.0.1:5000/search?search_author=Fredrick
```

## Step 6: Deactivate the Virtual Environment

To deactivate the virtual environment and return to your system's default Python environment, simply use the following command:

```
deactivate
```


## Troubleshooting

If you encounter any issues during the setup process, feel free to open an issue in this repository.

Happy Flask development!




# Dockerized Application

This repository contains a Dockerfile and necessary configuration to build and run the Dockerized version of the "Your Application Name" application.

## Prerequisites

Before you proceed with the Docker setup, make sure you have the following installed on your machine:

- Docker: [Install Docker](https://docs.docker.com/get-docker/)

## Building the Docker Image

To build the Docker image for the application, run the following command from the root of this repository:

```
docker build -t flask_app .
```

## Running the Docker Container

Once the Docker image is built, you can run the application in a Docker container using the following command:

```
docker run -p 5000:5000 -d flask_app
```

This command will start the application inside a Docker container, and it will be accessible in your web browser at.
```
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
```
## Stopping the Docker Container

To stop the running Docker container, you can use the following command:

```
docker stop <IMAGE NAME>
```
GET THE IMAGE NAME BY
```
docker PS
```

## Removing the Docker Image

If you want to remove the Docker image from your system, use the following command:

```
docker rmi flask_app:latest
```

## Customization


If your application requires specific environment variables or configuration options, you can modify the `Dockerfile` or use Docker Compose to manage multiple services.

## Troubleshooting

If you encounter any issues or have questions related to this Dockerized setup, please don't hesitate to open an issue in this repository.

Happy Dockerizing!
