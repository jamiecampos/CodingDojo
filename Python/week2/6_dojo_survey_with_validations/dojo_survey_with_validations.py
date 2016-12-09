from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'secret key'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def users():
    data = request.form

    if len(request.form['name']) < 1:
        flash("Name cannot be empty.")
        return redirect('/')
    elif len(request.form['comments']) < 1:
        flash ("Comments field cannot be empty.")
        return redirect('/')
    elif len(request.form['comments']) > 120:
        flash ("Comments must be fewer than 120 characters.")
        return redirect('/')
    else:
        print data
        return render_template('users.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)
