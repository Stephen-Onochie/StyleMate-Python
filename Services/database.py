import firebase_admin
import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('Assets/.env')

load_dotenv(dotenv_path=dotenv_path)

APIKEY = os.getenv('DATABASE_URL')


cred_obj = firebase_admin.credentials.Certificate('....path to file')
default_app = firebase_admin.initialize_app(cred_obj, {
    'databaseURL': APIKEY
})