# Start with an official Python runtime as a parent image (make sure to use the same version as during development)
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install necessary packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Streamlit uses
EXPOSE 8501

# Run the Streamlit app
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]