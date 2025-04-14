import logging
from flask import Flask, request

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Add this if not present:
logging.getLogger("pyroscope").setLevel(logging.DEBUG)

import pyroscope

import os
os.environ["PYROSCOPE_LOG_LEVEL"] = "debug"

# Initialize Pyroscope client
pyroscope.configure(
  application_name = "encode-service", # replace this with some name for your application
  server_address   = "http://pyroscope-agen.observability.svc.cluster.local", # replace this with the address of your Pyroscope server
)


app = Flask(__name__)

# Log request path before reaching any route handler
@app.before_request
def log_request_info():
    logger.info(f"Incoming request path: {request.path}")

@app.route('/hello')
def hello():
    return {"message": "Hello, encode Service !"}

if __name__ == '__main__':
app.run(host='0.0.0.0', port=5000, debug=True)

