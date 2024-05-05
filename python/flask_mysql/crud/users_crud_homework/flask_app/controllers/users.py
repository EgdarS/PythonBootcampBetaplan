from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.user import User

@app.route('/')
def controller():
    return redirect('/register')

@app.route('/register')
def registerPage():
    return render_template('newUser.html')

@app.route('/register/user', methods = ['POST'])
def registerUser():
    data = {
        'username': request.form['username'],
        'email' : request.form['email'],
        'password': request.form['password']
    }
    User.createUser(data)
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    users = User.getAllUsers()
    return render_template('allUsers.html', users=users)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')