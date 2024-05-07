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

@app.route('/profile/<int:id>')
def profile(id):
    data={
        'id':id
    }
    user=User.get_user_by_id(data)
    return render_template('profile.html', user=user)

@app.route('/edit/user/<int:id>')
def editProfile(id):
    data={
        'id':id
    }
    user=User.get_user_by_id(data)
    return render_template('editUser.html', user=user)

@app.route('/update/user/<int:id>')
def update(id):
    data = {
        'username': request.form['username'],
        'email' : request.form['email'],
        'password': request.form['password']
    }
    user=User.user_update(data)
    return redirect('/dashboard',user = user)

@app.route('/delete/<int:id>')
def delete(id):
    data={
        'id':id
    }
    user=User.user_delete(data)
    return redirect('/dashboard')
    #return redirect (request.referrer)  (reload tek e njejta faqe ne vend te redirect dashboard)

@app.route('/update/user/<int:id>', methods=['POST'])
def updateuser(id):
    data={
        'id': id,
        'username': request.form['username'],
        'email': request.form['email']
    }
    User.update_user(data)
    return redirect('/profile/'+ int(id))
    # return redirect ('/dashboard')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')