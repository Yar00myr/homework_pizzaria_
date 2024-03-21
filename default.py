from .. import app
from flask import render_template

@app.route('/')
def bese():
    return render_template('_base.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')