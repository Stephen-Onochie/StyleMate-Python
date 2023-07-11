import firebase_admin
from firebase_admin import db, credentials
import json
import os
from dotenv import load_dotenv
from pathlib import Path

# authenticate to firebase
cred_obj = credentials.Certificate('credentials.json')
firebase_admin.initialize_app(cred_obj, {
    "databaseURL": "https://stylemate-2f1e9-default-rtdb.firebaseio.com/"
})

# creating reference to root node
ref = db.reference("/")

# retrieving data from root node
ref.get()

