# Use Python 3.9 as the base image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the app.py file into the container
COPY app.py /app/

# Install Flask
RUN pip install flask

# Expose port 5000 to access the Flask app
EXPOSE 5000

# Define the command to run the app
CMD ["python", "app.py"]
