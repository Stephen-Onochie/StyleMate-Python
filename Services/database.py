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
def timestamp_format(timestamp=datetime.datetime.now().timestamp()):
    datetime_object = datetime.datetime.fromtimestamp(timestamp)
    formatted_timestamp = datetime_object.strftime('%Y-%m-%dT%H:%M:%SZ')
    return formatted_timestamp


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
        'clothes': {''},
        'outfits': {''}

    })


# adds a clothing item to a user's wardrobe
# Done Add code to add a clothing item
# TODO Add code to shorten image link if too long
def add_clothing(username, category, color, image):
    new_user_ref = ref.child('users').child(username).child('clothes').child(randomID())

    new_user_ref.set({
        'category': category,
        'color': color,
        'image': image,
        'timestamp': datetime.datetime.now().timestamp()
    })


# added new outfit to a user's wardrobe
# DONE Add code to save desired clothing items as an outfit
def add_outfit(username, name, clothes_id):
    new_user_ref = ref.child('users').child(username).child('outfits').child(randomID())
    clothes = ''

    # searches & saves clothing item object
    clothes_found = ref.child('users').child(username).child('clothes').get()
    clothes_ids = list(clothes_found.keys())
    for key in clothes_ids:
        if key == str(clothes_id):
            # use clothes_found[key] to access clothes item data
            clothes = key
            break

    # adds object/s to new outfit
    new_user_ref.set({
        'clothes': {0: clothes},
        'name': name,
        'timestamp': timestamp_format()
    })
    print('Outfit Created')


# updates a user's zipcode
# Done Add code to change a user's zipcode
def update_zipcode(username, new_zipcode):
    new_user_ref = ref.child('users').child(username)
    new_user_ref.update({
        'zipcode': new_zipcode
    })
    print('Zipcode Updated!')


# updates a user's name
# TODO Add code to change a user's name
def update_name(username, new_name):
    new_user_ref = ref.child('users').child(username)
    new_user_ref.update({
        'name': str(new_name)
    })
    print('Name Updated!')


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

# only runs testing code if program is directly run
if __name__ == "__main__":
    main()
