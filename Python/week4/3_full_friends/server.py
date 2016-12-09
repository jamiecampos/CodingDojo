from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def index():
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends=friends)

# Action of adding new friend, returning to homepage
@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'occupation': request.form['occupation']
           }
    mysql.query_db(query, data)
    return redirect('/')

# Edit page
@app.route('/friends/<id>/edit')
def edit(id):
    query = "SELECT * FROM friends WHERE id = :specific_id"
    data = {'specific_id': id}
    friends = mysql.query_db(query, data)
    return render_template('edit.html', all_friends=friends)

# Action of updating a friend, returning to homepage
@app.route('/friends/<id>', methods=['POST'])
def update(id):
    query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation WHERE id = :specific_id"
    data = {
             'specific_id': id,
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'occupation': request.form['occupation']
           }
    mysql.query_db(query, data)
    return redirect('/')

# Action of deleting a friend, returning to homepage
@app.route('/friends/<id>/delete', methods=['GET', 'POST'])
def delete(id):
    query = "DELETE FROM friends WHERE id = :specific_id"
    data = {'specific_id': id}
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
