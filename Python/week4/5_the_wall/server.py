from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[a-zA-Z]')
app = Flask(__name__)
app.secret_key = "secret"
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'the_wall')

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
    user = mysql.query_db(query, data)
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
        mysql.query_db(query, data)
        query2 = "SELECT * FROM users WHERE email = :email"
        data2 = {
                'email': request.form['email'],
                }
        user = mysql.query_db(query2, data2)
        session['user_key'] = user[0]['id']
        return redirect('/wall')

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
        session['user_key'] = user[0]['id']
        return redirect('/wall')
    else:
        error = True
        flash("Invalid login credentials.", "login")

    return redirect('/')

@app.route('/wall')
def wall():
    if 'user_key' not in session:
        return redirect('/')
    else:
        query = "SELECT first_name FROM users WHERE id = :id"
        data = {
                'id': session['user_key']
        }
        names = mysql.query_db(query, data)[0]
        print names
        all_messages = mysql.query_db("SELECT messages.id, CONCAT(first_name, ' ', last_name, ' - ') AS author, DATE_FORMAT(messages.created_on, '%M %D %Y') AS date, message AS msg_text, messages.id FROM users JOIN messages ON users.id = messages.user_id ORDER BY messages.created_on DESC")
        all_comments = mysql.query_db("SELECT messages.id, CONCAT(first_name, ' ', last_name, ' - ') AS author, DATE_FORMAT(comments.created_on, '%M %D %Y') AS date, comment AS comm_text, comments.message_id FROM users JOIN comments ON users.id = comments.user_id JOIN messages ON messages.id = comments.message_id ORDER BY comments.created_on ASC")
        return render_template('wall.html', names = names, all_messages = all_messages, all_comments = all_comments)

@app.route('/message', methods=['POST'])
def message():
    error = False
    if 'user_key' not in session:
        return redirect('/')
    elif len(request.form['post_message']) < 1:
        error = True
        flash("Please enter a message first.", "post_message")
    else:
        query = "INSERT INTO messages (message, user_id, created_on, modified_on) VALUES (:message, :user_id, NOW(), NOW());"
        data = {
            'message': request.form['post_message'],
            'user_id': session['user_key']
            }
        mysql.query_db(query, data)

    return redirect('/wall')

@app.route('/comment', methods=['POST'])
def comment():
    print request.form['msg_id']
    error = False
    if 'user_key' not in session:
        return redirect('/')
    elif len(request.form['post_comment']) < 1:
        error = True
        flash("Please enter a comment first.", "post_comment")
    else:
        query = "INSERT INTO comments (comment, created_on, modified_on, user_id, message_id) VALUES (:comment, NOW(), NOW(), :user_id, :message_id)"
        data = {
            'comment': request.form['post_comment'],
            'user_id': session['user_key'],
            'message_id': request.form['msg_id'],
        }
        mysql.query_db(query, data)

    return redirect('/wall')

@app.route('/logout')
def logout():
    session.pop('user_key', None)
    return redirect('/')

app.run(debug=True)
