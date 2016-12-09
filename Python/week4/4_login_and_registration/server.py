from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[a-zA-Z]')
app = Flask(__name__)
app.secret_key = "secret"
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'logindb')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def users():
    error = False
    registered = False
    query = "SELECT * FROM users WHERE email = :input_email"
    data = {
            'input_email': request.form['email'],
            }
    if len(mysql.query_db(query, data)) > 0:
        registered = True
        flash("Email already registered. Please log in.", "email")
    else:
        if len(request.form['first_name']) < 2:
            error = True
            flash("First name must be at least two characters.", "first_name")
        elif not NAME_REGEX.match(request.form['first_name']):
            error = True
            flash("First name must not be blank.", "first_name")

        if len(request.form['last_name']) < 2:
            error = True
            flash("Last name must be at least two characters.", "last_name")
        elif not NAME_REGEX.match(request.form['last_name']):
            error = True
            flash("Last name must not be blank.", "last_name")

        if len(request.form['email']) < 1:
            error = True
            flash("Email must not be blank.", "email")
        elif not EMAIL_REGEX.match(request.form['email']):
            error = True
            flash("Email address is not valid.", "email")

        if len(request.form['password']) < 8:
            error = True
            flash("Password must be at least eight characters.", "password")

        if request.form['confirm_password'] != request.form['password']:
            error = True
            flash("Field must match password.", "confirm_password")

    if not error and not registered:
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        query = "INSERT INTO users (first_name, last_name, email, password, created_on, modified_on) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW());"
        data = {
                'first_name': request.form['first_name'],
                'last_name':  request.form['last_name'],
                'email': request.form['email'],
                'password': pw_hash,
        }
        session['first_name'] = request.form['first_name']
        mysql.query_db(query, data)
        return redirect('/success')

    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    error = False
    password = request.form['login_password']
    query = "SELECT * FROM users WHERE email = :input_email"
    data = {
            'input_email': request.form['login_email'],
            }
    user = mysql.query_db(query, data)
    if len(user) > 0 and bcrypt.check_password_hash(user[0]['password'], password):
        session['email'] = request.form['login_email']
        return redirect('/success')
    else:
        error = True
        flash("Invalid login credentials.", "login")

    return redirect('/')

@app.route('/success')
def success():
    return render_template('success.html')

app.run(debug=True)
