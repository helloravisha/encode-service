import logging
from flask import Flask, request

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

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

