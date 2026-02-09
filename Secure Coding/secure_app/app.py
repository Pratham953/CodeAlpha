from flask import Flask, request
import os
from database import get_user_secure

app = Flask(__name__)

# Secret key from environment variable
app.secret_key = os.getenv("SECRET_KEY", "default_fallback_key")

@app.route("/")
def home():
    return "Welcome to Secure App"

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    # Input validation
    if not username or not password:
        return "Invalid input", 400

    user = get_user_secure(username, password)

    if user:
        return "Login Successful"
    else:
        return "Login Failed", 401

if __name__ == "__main__":
    # Debug disabled
    app.run(debug=False)
