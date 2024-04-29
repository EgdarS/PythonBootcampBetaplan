from flask_app import app
from flask import render_template, redirect, session, request


@app.route('/')
def index():
    view_count = session.get('view_count', 0)
    return render_template('index.html', view_count=view_count)

@app.route('/click', methods=['POST'])
def click():
    session['view_count'] = session.get('view_count', 0) + 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return render_template('reset.html')