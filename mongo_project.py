import os
import pymongo

if os.path.exists('env.py'):
    import env

MONGO_URI = os.environ.get('MONGO_URI')
DATABASE = 'myFirstDB'
COLLECTION = 'celebrities'


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print('Mongo is working')
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("not working bitch: %e") %e


def show_menu():
    print('')
    print('1. Add a record')
    print('2. Find a record by name')
    print('3. Edit a record')
    print('4. Delete a record')
    print('5. Exit')

    option = input('Enter option:')
    return option


def add_record():
    print('')
    first = input('Enter first name')
    last = input('Enter last name')
    dob = input('Enter Date of birth DD/MM/YYYY')
    hair_color = input('Enter hair color')
    occupation = input('Enter occupation')
    nationality = input('Enter country of origin')

    new_doc = {
        'first': first.lower(),
        'last': last.lower(),
        'dob': dob,
        'hair_color': hair_color.lower(),
        'occupation': occupation.lower(),
        'nationality': nationality.lower()
    }

    try:
        coll.insert(new_doc)
        print('')
        print('Success')
    except:
        print('Dupa')


def main_loop():
    while True:
        option = show_menu()
        if option == '1':
            add_record()
        elif option == '2':
            print('You have selected 2')
        elif option == '3':
            print('You have selected 3')
        elif option == '4':
            print('You have selected 4')
        elif option == '5':
            conn.close()
            break
        else:
            print('Invalid option')
        print('')


conn = mongo_connect(MONGO_URI)
coll = conn[DATABASE][COLLECTION]
main_loop()
