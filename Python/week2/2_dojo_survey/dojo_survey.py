from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    return render_template('result.html')

app.run(debug=True)
