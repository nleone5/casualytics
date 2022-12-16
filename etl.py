import os
import json
import pymongo
import pandas as pd

# Connecting to MongoDB
# ---------------------------------------------------------------- #
try:
    # Establishing Connection to localhost and Port the DB is Running On
    mongo = pymongo.MongoClient(
        host = 'localhost',
        port = 27017,
        serverSelectionTimeoutMS = 1000
    )
    print (' * Success - Connection Established to the Server.')
    # Selecting Our DB and Creating if Not Exist
    db = mongo.MLB
    print(' * Success - DB Selected.')
    mongo.server_info()
    print(' * Success - Connection Established to the DB.')
except:
    print('ERROR - Could Not Connect to the DB.')

# Inserting Each File into the DB
# ---------------------------------------------------------------- #
# Setting Env Path to Data Directory

path = "data"
os.chdir(path)

retval = os.getcwd()

print("* Current working directory")

print(retval)

try: 

    
    # Creating DF, Turning CSV to Dict, and Inserting into Colelction
    df = pd.read_csv('Hitters.csv')
    print(' * Success - Hitters Data Has Been Read.')
    mongoDict = df.to_dict(orient = "records")
    db.MLB.Hitters.insert_many(mongoDict)
    print(' * Success - Hitters Data Has Been Inserted into the DB.')

    df = pd.read_csv('Pitchers.csv')
    mongoDict = df.to_dict(orient = "records")
    db.MLB.Pitchers.insert_many(mongoDict)

    print(' * Success - All Data Has Been Inserted into the DB.')
except:
    print(' * Failure - The Data Could Not Be Inserted to the DB.')