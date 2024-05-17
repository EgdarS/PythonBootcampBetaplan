from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

@app.route('/ninjas', methods=['POST'])
def createNinja():
    data={
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojo_id': request.form['dojo_id']
    }
    Ninja.createNinja(data)
    return redirect ('/dojos')
