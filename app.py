import logging
from flask import Flask, request

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

import pyroscope

# Initialize Pyroscope client
pyroscope.configure(
    app_name="encode-service",  # You can use a name for your service
    server_url="http://a2074f890eaab46f7a87182611724d46-1127988196.us-east-2.elb.amazonaws.com"  # Make sure this points to your Pyroscope server
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
    app.run(host='0.0.0.0', port=5000)

