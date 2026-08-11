from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    today = datetime.now()

    return render_template('index.html', today=today)

@app.route('/api/<firstname>/<lastname>')
def second(firstname, lastname):
    return f'Welcome to second page:Hi {firstname} {lastname}'


@app.route('/api/personal')
def personal():
    name = request.values.get('name')
    age = request.values.get('age')

    result = {
        'name': name,
        "age": age
    }

    return result

if __name__ == '__main__':
    app.run(debug=True)
    # app.run()
