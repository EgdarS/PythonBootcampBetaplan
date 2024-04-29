from flask_app import app
from flask import render_template, redirect, session, request
import random
import datetime


@app.route('/')
def index():
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'goldAmount' not in session:
        session['goldAmount'] = 0
        session['activities'] = []
    return render_template('dashboard.html')

@app.route('/process_money', methods = ['POST'])
def process_money():
    type = request.form['type']
    if type == 'farm':
        mywinnings=random.randint(10,20)
        activity={
            'message': f'Earned {mywinnings} gold from the farm. ({datetime.datetime.now()})',
            'amount': mywinnings
        }
        session['activities'].append(activity)
    elif type == 'cave':
        mywinnings=random.randint(5,10)
        activity={
            'message': f'Earned {mywinnings} gold from the cave. ({datetime.datetime.now()})',
            'amount' : mywinnings
        }
        session['activities'].append(activity)
    elif type == 'house':
        mywinnings=random.randint(2,5)
        activity={
            'message': f'Earned {mywinnings} gold from the house. ({datetime.datetime.now()})',
            'amount' : mywinnings
        }
        session['activities'].append(activity)
    elif type == 'casino':
        mywinnings=random.randint(-50,50)
        if mywinnings >=0:
            activity = {
                'message': f'Entered a casino and won {mywinnings} golds. ({datetime.datetime.now()})',
                'amount': mywinnings
            }
            session['activities'].append(activity)
        else:
            activity = {
                'message': f'Entered a casino and lost {mywinnings} golds. ({datetime.datetime.now()})',
                'amount': mywinnings
            }
            session['activities'].append(activity)
    session['goldAmount'] += mywinnings
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')