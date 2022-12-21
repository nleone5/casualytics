import stats.statsapi as statsapi
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



@app.route("/", methods = ['GET', 'POST'])

def index():

    if request.method == 'POST':
        # Getting Form Data
        Double = request.form.get('2B')
        Triple = request.form.get('3B')
        AB = request.form.get('AB')
        AVG = request.form.get('AVG')
        Age = request.form.get('Age')
        BB = request.form.get('BB')
        CS = request.form.get('CS')
        G = request.form.get('G')
        H = request.form.get('H')
        HBP = request.form.get('HBP')
        HR = request.form.get('HR')
        OBP = request.form.get('OBP')
        OPS = request.form.get('OPS')
        Player = request.form.get('Name')
        Pos = request.form.get('Pos')
        RBI = request.form.get('RBI')
        R = request.form.get('R')
        SB = request.form.get('SB')
        SLG = request.form.get('SLG')
        SO = request.form.get('SO')
        TB = request.form.get('TB')
        Team = request.form.get('Team')

        # Inserting Data into DB
        db.MLB.insert_one({
            '2B': Double,
            '3B': Triple,
            'AB': AB,
            'AVG': AVG,
            'Age': Age,
            'BB': BB,
            'CS': CS,
            'G': G,
            'H': H,
            'HBP': HBP,
            'HR': HR,
            'OBP': OBP,
            'OPS': OPS,
            'Name': Player,
            'Pos': Pos,
            'RBI': RBI,
            'R': R,
            'SB': SB,
            'SLG': SLG,
            'SO': SO,
            'TB': TB,
            'Team': Team
        })
        return redirect(url_for('index'))
    else:
        # Getting Data from DB
        players = db.MLB.find()
        return render_template('index.html', players = players)   
    
# Read

@app.route("/read/<player_id>")
def read(player_id):
    player = db.MLB.find_one({'_id': ObjectId(player_id)})
    return render_template('read.html', player = player)
    
# Update

@app.route("/update/<player_id>", methods = ['GET', 'POST'])

def update(player_id):
    if request.method == 'POST':
        # Getting Form Data
        Double = request.form.get('2B')
        Triple = request.form.get('3B')
        AB = request.form.get('AB')
        AVG = request.form.get('AVG')
        Age = request.form.get('Age')
        BB = request.form.get('BB')
        CS = request.form.get('CS')
        G = request.form.get('G')
        H = request.form.get('H')
        HBP = request.form.get('HBP')
        HR = request.form.get('HR')
        OBP = request.form.get('OBP')
        OPS = request.form.get('OPS')
        Player = request.form.get('Name')
        Pos = request.form.get('Pos')
        RBI = request.form.get('RBI')
        R = request.form.get('R')
        SB = request.form.get('SB')
        SLG = request.form.get('SLG')
        SO = request.form.get('SO')
        TB = request.form.get('TB')
        Team = request.form.get('Team')

        # Updating Data in DB
        db.MLB.update_one(
            {'_id': ObjectId(player_id)},
            {'$set': {
                '2B': Double,
                '3B': Triple,
                'AB': AB,
                'AVG': AVG,
                'Age': Age,
                'BB': BB,
                'CS': CS,
                'G': G,
                'H': H,
                'HBP': HBP,
                'HR': HR,
                'OBP': OBP,
                'OPS': OPS,
                'Name': Player,
                'Pos': Pos,
                'RBI': RBI,
                'R': R,
                'SB': SB,
                'SLG': SLG,
                'SO': SO,
                'TB': TB,
                'Team': Team
            }}
        )
        return redirect(url_for('index'))
    else:
        # Getting Data from DB
        player = db.MLB.find_one({'_id': ObjectId(player_id)})
        return render_template('update.html', player = player)



