Containerizing your Streamlit app with Docker helps you package it with all its dependencies to run consistently across different environments. Here’s a step-by-step guide:

### 1. Create a `Dockerfile`

Create a file named `Dockerfile` in the same directory as your app. This file will contain instructions for building the Docker image.

**Example `Dockerfile`:**
```Dockerfile
# Start with an official Python runtime as a parent image (make sure to use the same version as during development)
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install necessary packages
RUN pip install -r requirements.txt

# Expose the port that Streamlit uses
EXPOSE 8501

# Run the Streamlit app
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### 2. Create a `requirements.txt` File

List all the Python packages required by your app in a `requirements.txt` file:

```bash
pip freeze > requirements.txt
```

### 3. Build the Docker Image

Run the following command in your terminal (in the same directory as your `Dockerfile`):

```bash
docker build -t my-st-app .
```

- `-t my-st-app` tags the image as `my-st-app`.
- `.` specifies the current directory as the build context.

### 4. Run the Docker Container

Use the following command to start the container:

```bash
docker run --name st-app-container -p 8501:8501 my-st-app
```
- `--name st-app-container` assigns the st-app-container to your running container.
- `-p 8501:8501` maps the container’s port 8501 to your machine’s port 8501.
- `my-st-app` is the name of the image you just built.

### 5. Access Your App

Open a web browser and navigate to:

```
http://localhost:8501
```

You should see your Streamlit app running in the browser.