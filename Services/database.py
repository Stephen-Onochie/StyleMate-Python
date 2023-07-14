import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
import random
import datetime
import time

# Reference 1 => https://www.freecodecamp.org/news/how-to-get-started-with-firebase-using-python/
# Reference 2 => https://firebase.google.com/docs/database/admin/save-data

# Fetch the service account key JSON file contents
cred = credentials.Certificate('/Users/stephenonochie/Documents/GitHub/StyleMate-Python/Assets/key.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://stylemate-2f1e9-default-rtdb.firebaseio.com/'
})

# As an admin, the app has access to read and write all data, regardless of Security Rules
ref = db.reference('/')


# generates a random 9 number string id for reference
def randomID():
    id = ''
    for i in range(0, 9):
        id += str(random.randint(0, 9))
    return id


# generates a timestamp in a custom format
def timestamp():
    pass


# resets entire database with new schema
# TODO Add on to function to save last database screenshot as a json file
def reset():
    with open("/Users/stephenonochie/Documents/GitHub/StyleMate-Python/Assets/References/set.json", "r") as f:
        file_contents = json.load(f)
    ref.set(file_contents)


# adds a new user to the database
# Done Add code to add a new user
def add_user(username, fullname, zipcode):
    new_user_ref = ref.child('users').child(username)

    new_user_ref.set({
        'name': fullname,
        'zipcode': str(zipcode),
        'clothes': {},
        'outfits': {}

    })


# adds a clothing item to a user's wardrobe
# Done Add code to add a clothing item
def add_clothing(username, category, color, image):
    new_user_ref = ref.child('users').child(username).child('clothes').child(randomID())

    new_user_ref.set({
        'category': category,
        'color': color,
        'image': image,
        'timestamp': datetime.datetime.now().timestamp()
    })


# adds an entire outfit to a user's wardrobe
# TODO Add code to save desired clothing items as an outfit
def add_outfit():
    pass


# updates a user's zipcode
# TODO Add code to change a user's zipcode
def update_zipcode():
    pass


# updates a user's name
# TODO Add code to change a user's name
def update_name():
    pass


# updates a user's clothing item information
# TODO Add code to change a clothing item info
def update_clothing():
    pass


# updates a user's outfit / outfit info
# TODO Add code to change an outfit or its information
def update_outfit():
    pass


# deletes a user from the database
# TODO Add code to delete a user
def delete_user():
    pass


# deletes a clothing item from a user's wardrobe
# TODO Add code to delete a clothing item
def delete_clothing():
    pass


# deletes an outfit from a user's wardrobe
# TODO Add code to delete an outfit
def delete_outfit():
    pass


# testing code here
def main():
    add_clothing('stephenO', 'Shirt', 'Red', 'data:image/webp;base64,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')


# only runs testing code if program is directly run
if __name__ == "__main__":
    main()
