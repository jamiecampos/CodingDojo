from flask import Flask, render_template, request, redirect
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = 'Secret key'

mysql = MySQLConnector(app, "email_validation_with_db")

@app.route('/')
def index():
    results = mysql.query_db('SELECT * FROM emails')
    return render_template('index.html', results=results)

@app.route('/process', methods=["POST"])
def process():
    email = request.form['email']
    errors = []
    query = "INSERT INTO emails (email, created_on, modified_on) VALUES (:email, NOW(), NOW())"
    data = {
    'email': request.form['email']
    }

    if len(email) < 1:
        errors.append("Email must be at least one character.")
    elif not EMAIL_REGEX.match(request.form['email']):
        errors.append("Email address is not valid.")

    if len(errors) > 0:
        return render_template('index.html', errors=errors)
    else:
        query = "SELECT email, created_on FROM emails"
        data = {
        'email': request.form['email']
        }
        results = mysql.query_db(query, data)
        return render_template('success.html', results = results, last = request.form['email'])

app.run(debug=True)
