from distutils.log import debug
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes



@app.route('/')
def index():
    if 'count' in session:
        pass
    else:
        session['count'] = 0
    return render_template('index.html')


@app.route('/up')
def count():
    session['count'] += 1
    return redirect('/')

@app.route('/down')
def down():
    session['count'] -= 1
    return redirect('/')
 

@app.route('/destroy_session')
def destroy():
    session.clear()
    print(session)
    return redirect('/')
 
if __name__=="__main__":
    app.run(debug=True)