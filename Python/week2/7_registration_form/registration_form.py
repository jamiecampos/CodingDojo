from flask import Flask, render_template, request
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=["POST"])
def process():
    email = request.form['email']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    errors = []

    if len(email) < 1:
        errors.append("Email must be at least one character.")
    elif not EMAIL_REGEX.match(request.form['email']):
        errors.append["Email address is not valid."]

    if len(first_name) < 1:
        errors.append("First name must be at least one character.")
        
#     Try to do this using regex! https://www.debuggex.com/cheatsheet/regex/python
    else:
        for i in range(len(first_name)):
            if ord(first_name[i]) > 47 and ord(first_name[i]) < 58:
                errors.append("First name cannot contain a number.")
                break

    if len(last_name) < 1:
        errors.append("Last name must be at least one character.")
#     Try to do this using regex! https://www.debuggex.com/cheatsheet/regex/python
    else:
        for i in range(len(last_name)):
            if ord(last_name[i]) > 47 and ord(last_name[i]) < 58:
                errors.append("Last name cannot contain a number.")
                break

    if len(password) < 9:
        errors.append("Password must be at least nine characters.")

    if confirm_password != password:
        errors.append("Confirm password must match password.")

    if len(errors) > 0:
        return render_template('index.html', errors=errors)
    else:
        errors.append("Everything was okay!")
        return render_template('index.html', errors=errors)

app.run(debug=True)
