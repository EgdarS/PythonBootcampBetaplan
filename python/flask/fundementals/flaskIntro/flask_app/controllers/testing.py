from flask_app import app
from flask import render_template, redirect

@app.route('/')
def dashboard():
    users = [
   {'first_name' : 'Michael', 'last_name' : 'Choi'},
   {'first_name' : 'John', 'last_name' : 'Supsupin'},
   {'first_name' : 'Mark', 'last_name' : 'Guillen'},
   {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
    return render_template("dashboard.html", users = users)

@app.route('/profile/<int:id>')
def profile(id):
    users = [
   {'first_name' : 'Michael', 'last_name' : 'Choi'},
   {'first_name' : 'John', 'last_name' : 'Supsupin'},
   {'first_name' : 'Mark', 'last_name' : 'Guillen'},
   {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
    return render_template("profile.html", users = users[-1])

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def loginPage():
    return render_template('login.html')

@app.route('/login', method= ['POST'])
def loginUser():
    return redirect('/')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/hello/<int:name>')
def hello(name):
    return f'Hello {name}'