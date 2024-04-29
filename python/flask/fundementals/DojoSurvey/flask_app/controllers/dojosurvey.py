from flask_app import app
from flask import render_template, redirect, session, request

@app.route('/')
def index():
    return render_template('submitform.html')

@app.route('/process', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['yourlocation']
        language = request.form['favouritelanguage']
        comment = request.form['comment']
        session['name'] = name
        session['location'] = location
        session['language'] = language
        session['comment'] = comment
        return redirect('/result')
    
@app.route('/result')
def result():
    name = session.get('name')
    location = session.get('location')
    language = session.get('language')
    comment = session.get('comment')
    return render_template('submittedinfo.html', name=name, location=location, language=language, comment=comment)

