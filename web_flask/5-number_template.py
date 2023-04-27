#!/usr/bin/python3
"""script that starts a Flask web application:
web application must be listening on `0.0.0.0`, port `5000`
Routes:
/: display `“Hello HBNB!”`
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of the text variable
(replace underscore _ symbols with a space )
/python/(<text>): display “Python ”, followed by the value of the text variable
(replace underscore _ symbols with a space )
The default value of text is “is cool”
/number/<n>: display “n is a number” only if n is an integer
You must use the option `strict_slashes=False` in your route definition
"""


from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    return "HBNB"


@app.route('/c/<text>')
def show_c_text(text):
    return "C {}".format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def show_python_text(text="is cool"):
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes = False)
def number_template(n=89):
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
