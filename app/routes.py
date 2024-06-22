from app import app
from flask import jsonify


@app.route('/')
def home():
    return "Welcome to the Flask app!"


@app.route('/api/greet/<name>')
def greet(name):
    return jsonify(message=f"Hello, {name}!!!")
