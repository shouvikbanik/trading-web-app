"""This module programs the API route."""
from flask import jsonify
from app import app


@app.route('/')
def home():
    """Default dashboard"""
    return "Welcome to the Flask app!"


@app.route('/api/greet/<name>')
def greet(name):
    """Test api"""
    return jsonify(message=f"Hello, {name}!!!")
