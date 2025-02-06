from flask import Flask

# Create a Flask web application
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def hello():
    return 'Hello, World!'

# Define another route for /healthcheck
@app.route('/healthcheck')
def healthcheck():
    return 'OK', 200

# Entry point to start the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)  # Port 8080 is required on App Engine
