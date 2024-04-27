from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def play():
    return render_template('play.html')

@app.route('/play/<int:x>')
def playx(x):
    return render_template('playx.html', times=x)

@app.route('/play/<int:x>/<color>')
def playxy(x, color):
    return render_template('playxy.html', times=x, color=color)

if __name__ == '__main__':
    app.run(debug=True)
