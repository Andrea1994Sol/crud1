from flask import render_template
from src import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users')
def users():
    return render_template('users/create.html')

@app.route('/login')
def login():
    return render_template('users/login.html')