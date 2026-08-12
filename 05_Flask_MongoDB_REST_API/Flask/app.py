# pylint:disable=all
from flask import Flask, request, render_template
from datetime import datetime
from dotenv import load_dotenv
import os
import pymongo

load_dotenv()

MONGO_URI = os.getenv("MONGODB_URL")

print(MONGO_URI)

client = pymongo.MongoClient(MONGO_URI)

db = client.test

collection = db['flask-tutorial']

app = Flask(__name__)

@app.route('/')
def home():
    today = datetime.now()

    return render_template('index.html', today=today)

@app.route('/api/<firstname>/<lastname>')
def second(firstname, lastname):
    return f'Welcome to second page:Hi {firstname} {lastname}'


@app.route('/submit', methods=['POST'])
def submit():
    # name = request.form.get('name')
    # email = request.form.get('email')
    # password = request.form.get('password')
    # confirm_password = request.form.get('confirm_password')

    form_data = dict(request.form)

    collection.insert_one(form_data)

    return "Successfully"

@app.route('/view')
def view():
    data = list(collection.find())

    for item in data:
        print(item)
        del item['_id']
    
    # data = {
    #     'data': data
    # }

    return {
        'message':"Retreieved Successfully",
        'data' : data
    }

if __name__ == '__main__':
    app.run(debug=True)
    # app.run()
