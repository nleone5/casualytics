import datetime
from flask import Flask, render_template, request, url_for, redirect, session
from flask.globals import session
from flask.helpers import url_for
import pymongo
from bson.objectid import ObjectId
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'testing'

# Connecting to MongoDB
# ---------------------------------------------------------------- #
try:
    # Establishing Connection to localhost and Port the DB is Running On
    mongo = pymongo.MongoClient(
        host = 'localhost',
        port = 27017,
        serverSelectionTimeoutMS = 1000
    )
    # Selecting Our DB
    db = mongo.MLB
    mongo.server_info()
    print(' * Success - Database Running on localhost, port 27017')
except:
    print('ERROR - Could Not Connect to the DB.')

# CRUD Routes
# ---------------------------------------------------------------- #

# Create

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/insert', methods=['POST'])
def insert():
    # Creating a Dictionary to Store the Data
    data = {
        'name': request.form.get('name'),
        'team': request.form.get('team'),
        'position': request.form.get('position'),
        'dob': request.form.get('dob'),
        'height': request.form.get('height'),
        'weight': request.form.get('weight'),
        'bats': request.form.get('bats'),
        'throws': request.form.get('throws'),
        'debut': request.form.get('debut'),
        'salary': request.form.get('salary'),
        'image': request.form.get('image'),
        'bio': request.form.get('bio')
    }
    # Inserting the Data into the DB
    db.players.insert_one(data)
    print(' * Success - Data Inserted')
    return redirect(url_for('read'))

# Read

@app.route('/')
def read():
    # Retrieving All Data from the DB
    data = db.players.find()
    print(' * Success - Data Retrieved')
    return render_template('read.html', data=data)

# Update

@app.route('/update/<id>')
def update(id):
    # Retrieving Data from the DB
    data = db.players.find_one({'_id': ObjectId(id)})
    print(' * Success - Data Retrieved')
    return render_template('update.html', data=data)

@app.route('/edit', methods=['POST'])

def edit():
    # Creating a Dictionary to Store the Data
    data = {
        'name': request.form.get('name'),
        'team': request.form.get('team'),
        'position': request.form.get('position'),
        'dob': request.form.get('dob'),
        'height': request.form.get('height'),
        'weight': request.form.get('weight'),
        'bats': request.form.get('bats'),
        'throws': request.form.get('throws'),
        'debut': request.form.get('debut'),
        'salary': request.form.get('salary'),
        'image': request.form.get('image'),
        'bio': request.form.get('bio')
    }
    # Updating the Data in the DB
    db.players.update_one({'_id': ObjectId(request.form.get('id'))}, {'$set': data})
    print(' * Success - Data Updated')
    return redirect(url_for('read'))

# Delete

@app.route('/delete/<id>')
def delete(id):
    # Deleting the Data from the DB
    db.players.delete_one({'_id': ObjectId(id)})
    print(' * Success - Data Deleted')
    return redirect(url_for('read'))

# Running the App
# ---------------------------------------------------------------- #

if __name__ == '__main__':
    app.run(debug=True)
    