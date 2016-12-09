from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'very secret'

@app.route('/')
def counter():
    try:
        session['counter']
    except:
        session['counter'] = 0
    session['counter'] += 1
    return render_template('index.html')

app.run(debug=True)
