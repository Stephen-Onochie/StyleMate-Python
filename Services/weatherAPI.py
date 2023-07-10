# Needed libraries
import http.client
import json
import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('Assets/.env')

load_dotenv(dotenv_path=dotenv_path)

APIKEY = os.getenv('WEATHERAPI')

# connection to Weather API
api = http.client.HTTPConnection("weatherapi-com.p.rapidapi.com")

# Important keys for use
headers = {
    'X-RapidAPI-Key': APIKEY,
    'X-RapidAPI-Host': "weatherapi-com.p.rapidapi.com"
}