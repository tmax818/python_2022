import re
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/handle_form', methods=["POST"])
def handle_form():
    print(request.form)
    session['info'] = request.form['test']
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)