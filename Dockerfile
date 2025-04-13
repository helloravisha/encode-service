# Use Python 3.9 as the base image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the app.py file into the container
COPY app.py /app/

# Install Flask
RUN pip install flask pyroscope

# Expose port 5000 to access the Flask app
EXPOSE 5000

# Set environment variables for Pyroscope (adjust the URL as per your Pyroscope setup)
ENV PYROSCOPE_SERVER=http://pyroscope-server:4040

# Define the command to run the app
CMD ["python", "app.py"]
