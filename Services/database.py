import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json

# Reference 1 => https://www.freecodecamp.org/news/how-to-get-started-with-firebase-using-python/
# Reference 2 => https://firebase.google.com/docs/database/admin/save-data

# Fetch the service account key JSON file contents
cred = credentials.Certificate('/Users/stephenonochie/Documents/GitHub/StyleMate-Python/Assets/key.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://stylemate-2f1e9-default-rtdb.firebaseio.com/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('/')


# resets entire database with new schema
# TODO Add on to function to save last database screenshot as a json file
def reset():
    with open("/Users/stephenonochie/Documents/GitHub/StyleMate-Python/Assets/References/set.json", "r") as f:
        file_contents = json.load(f)
    ref.set(file_contents)


# updates a datapoint to desired value
# TODO Add code to change a datapoint
def update():
    pass


# adds a new user to the database
def add_user(username, fullname, zipcode):
    new_user_ref = ref.child('users').child(username)

    new_user_ref.set({
        'name': fullname,
        'zipcode': str(zipcode),
        'clothes': {},
        'outfits': {}

    })


# added the desired value to the database
# TODO Add code to send new data
def push():
    pass


# retrieves data from database
# TODO Add Code to get data values
def get():
    pass


# deletes a datapoint
# TODO Add code to delete a datapoint
def delete():
    pass


# testing code here
def main():
    reset()
    print(ref.get())


# only runs testing code if program is directly run
if __name__ == "__main__":
    main()
