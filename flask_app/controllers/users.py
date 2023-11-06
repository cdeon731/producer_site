from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import user
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/1test')
def next_page():
    return render_template('dashboard2.html')