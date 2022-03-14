from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=["POST"])
def process():
    print(request.form)
    session['name'] = request.form['name']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/success')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__=="__main__":
    app.run(debug=True)