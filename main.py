 
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    operation = request.form.get('operation')
    num1 = int(request.form.get('num1'))
    num2 = int(request.form.get('num2'))

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        result = num1 / num2

    return render_template('results.html', result=result)

@app.route('/save', methods=['POST'])
def save():
    operation = request.form.get('operation')
    num1 = int(request.form.get('num1'))
    num2 = int(request.form.get('num2'))
    result = int(request.form.get('result'))

    # Save the calculation to the database.

    return render_template('saved.html')

@app.route('/saved')
def saved():
    # Get the saved calculations from the database.

    return render_template('saved.html', calculations=calculations)

if __name__ == '__main__':
    app.run()
