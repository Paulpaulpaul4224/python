import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_bob():
    return "Hello Bob!"

if __name__ == "__main__":
    # Cloud Run passes the port as an environment variable
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=True, host="0.0.0.0", port=port)
