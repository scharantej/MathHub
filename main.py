 
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/problems')
def problems():
  return render_template('problems.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
  if request.method == 'POST':
    problem = request.form['problem']
    answer = request.form['answer']
    return render_template('solved.html', problem=problem, answer=answer)
  else:
    return render_template('submit.html')

@app.route('/solved')
def solved():
  return render_template('solved.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  if request.method == 'POST':
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    return render_template('contact.html', name=name, email=email, message=message)
  else:
    return render_template('contact.html')

if __name__ == '__main__':
  app.run(debug=True)
