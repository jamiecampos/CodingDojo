# Create a site that when a user loads it creates a random number between 1-100
# and stores the number in session. Allow the user to guess at the number and
# tell them when they are too high or too low. If they guess the correct number
# tell them and offer to play again.

from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'


@app.route('/')
def index():
    session['answer'] = random.randrange(0, 101)
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guess():
    guess = int(request.form['guess'])
    print guess
    print session['answer']
    print(guess>session['answer'])

    if session['answer'] < guess:
        message = "Too high!"

    elif session['answer'] > guess:
        message = "Too low!"

    else:
        message = "You're Right"

    return render_template('index.html', message = message)


app.run(debug=True)
