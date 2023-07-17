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
        'clothes': {},
        'outfits': {}
    })
    print('User Added!')


# adds a clothing item to a user's wardrobe
# Done Add code to add a clothing item
# TODO Add code to shorten image link if too long
def add_clothing(username, category, color, image):
    new_user_ref = ref.child('users').child(username).child('clothes').child(randomID())
    new_user_ref.set({
        'category': category,
        'color': color,
        'image': image,
        'timestamp': timestamp_format()
    })
    print('Clothing Added!')


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
    print('Outfit Created!')


# updates a user's zipcode
# Done Add code to change a user's zipcode
def update_zipcode(username, new_zipcode):
    new_user_ref = ref.child('users').child(username)
    new_user_ref.update({
        'zipcode': new_zipcode
    })
    print('Zipcode Updated!')


# updates a user's name
# Done Add code to change a user's name
def update_name(username, new_name):
    new_user_ref = ref.child('users').child(username)
    new_user_ref.update({
        'name': str(new_name)
    })
    print('Name Updated!')


# updates a user's clothing item information
# Done Add code to change a clothing item info
def update_clothing(username, clothing_id, category=0, color=0, image=0):
    new_user_ref = ref.child('users').child(username).child('clothes').child(str(clothing_id))
    new_category = ''
    new_color = ''
    new_image = ''

    if category != 0:
        new_category = category
        new_user_ref.update({
            'category': new_category
        })

    if color != 0:
        new_color = color
        new_user_ref.update({
            'color': new_color
        })

    if image != 0:
        new_image = image
        new_user_ref.update({
            'image': new_image
        })

    new_user_ref.update({
        'timestamp': timestamp_format()
    })

    print('Clothing Updated!')
    print(timestamp_format())


# updates a user's outfit / outfit info
# Done Add code to change an outfit or its information
def update_outfit(username, outfit_id, clothes_id=0, name=0):
    new_user_ref = ref.child('users').child(username).child('outfits').child(str(outfit_id))
    new_clothes = ''
    new_name = ''

    if clothes_id != 0:
        # search of last clothing_id key
        clothes_found = new_user_ref.child('clothes').get()
        new_key = len(clothes_found)
        print(new_key)
        # set new key as last key + 1
        new_user_ref.child('clothes').update({
            new_key: clothes_id
        })

    if name != 0:
        new_name = name
        new_user_ref.update({
            'name': new_name
        })

    new_user_ref.update({
        'timestamp': timestamp_format()
    })

    print('Outfit Created!')
    print(timestamp_format())


# deletes a user from the database
# Done Add code to delete a user
def delete_user(username):
    new_user_ref = ref.child('users').child(username)
    new_user_ref.delete()
    print('User Deleted!')


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
    delete_user('janeS')

# only runs testing code if program is directly run
if __name__ == "__main__":
    main()
