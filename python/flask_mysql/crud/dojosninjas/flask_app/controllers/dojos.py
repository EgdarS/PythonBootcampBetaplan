from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def controller():
    return redirect('/dojos')

@app.route('/dojos')
def dojo():
    dojos=Dojo.getAllDojos()
    data={
        'dojo_id':id
    }
    dojo = Dojo.get_dojo_by_id(data)
    return render_template('dojos.html', dojos=dojos, dojo=dojo)

@app.route('/dojos', methods = ['POST'])
def createDojo():
    data={
        'name': request.form['name']
    }
    Dojo.createDojo(data)
    return redirect('/dojos')

@app.route('/dojosninjas/<int:id>')
def dojosninjas(id):
    data={
        'id':id
    }
    dojo=Dojo.get_dojo_by_id(data)
    ninjas=Ninja.getAllNinjas(data)
    return render_template('dojosninjas.html', dojo=dojo, ninjas=ninjas)