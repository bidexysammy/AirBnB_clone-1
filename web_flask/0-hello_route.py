#!/usr/bin/python3
"""
Start Flask app with root route
"""

from flask import Flask
app = Flask(__name__)


@app.route("/airbnb-onepage", strict_slashes=False)
def hello_hbnb():
    """
    Returns a string saying hello
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=true)
