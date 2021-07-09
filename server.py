import re
from flask import Flask, render_template
from math import floor

app = Flask(__name__)

#  other stuff goes here

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/multiply/<int:x>/<int:y>')
def multiply(x, y):
    result = x * y
    return render_template('multiply.html', x = x, y = y, result = result)

# @app.route('/is_palindrome/<string:input_string>')
# def is_palindrome(input, string):
#     return "I am a second flask application hooray!"

@app.route('/multiplication_table/<int:x>/<int:y>')
def multiplication_table(x, y):
    results = []
    for j in range(1, y+1):
        results_row = []
        for i in range(1, x+1):
            results_row.append(i * j)
        results.append(results_row)

    print(results)
    return render_template('table.html', table = results)

if __name__ == "__main__":
    app.run(debug = True)