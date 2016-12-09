from flask import Flask, render_template
app = Flask(__name__)
app.secret_key= "secretkey"

turtles = {'purple':'donatello.jpg', 'blue':'leonardo.jpg', 'orange':'michelangelo.jpg', 'red':'raphael.jpg', 'april':'notapril.jpg'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    return render_template('ninja.html')

@app.route('/ninja/<color>')
def ninja_color(color):
    if color == 'purple' or color == 'blue' or color == 'orange' or color == 'red':
        return render_template('ninja_color.html', color=turtles[color])
    else:
        return render_template('ninja_color.html', color=turtles['april'])

app.run(debug=True)
