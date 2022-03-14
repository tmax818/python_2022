from flask import Flask, render_template, session, request, redirect
import random

app = Flask(__name__)

app.secret_key = "I am the princess of Canada"


@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randint(1,101)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    print(request.form['number'])
    if int(request.form['number']) > int(session['number']):
        session['message'] = 'too high'
    elif int(request.form['number']) < int(session['number']):
        session['message'] = 'too low'
    else:
        session['message'] = 'you got it!!'
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)