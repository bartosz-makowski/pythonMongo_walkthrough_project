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
    print('5. See all data')
    print('6. Exit')

    option = input('Enter option:')
    return option


def get_record():
    print('')
    first = input('Enter first name > ')
    last = input('Enter last name > ')

    try:
        doc = coll.find_one({'first': first.lower(), 'last': last.lower()})
        print(doc)
    except:
        print('Error accessing the database')

    if not doc:
        print('')
        print('no results found')

    return doc



def add_record():
    print('')
    first = input('Enter first name > ')
    last = input('Enter last name > ')
    dob = input('Enter Date of birth DD/MM/YYYY > ')
    hair_color = input('Enter hair color > ')
    occupation = input('Enter occupation > ')
    nationality = input('Enter nationality > ')

    new_doc = {
        'first': first.lower(),
        'last': last.lower(),
        'dob': dob,
        'hair_color': hair_color.lower(),
        'occupation': occupation.lower(),
        'nationality': nationality.lower()
    }

    try:
        coll.insert_one(new_doc)
        print('')
        print('Success')
    except:
        print('Dupa')


def check_all():
    documents = coll.find()
    for doc in documents:
        print(doc)


def find_record():
    doc = get_record()
    if doc:
        print('')
        for k,v in doc.items():
            if k!= "_id":
                print(k.capitalize() + ': ' + v.capitalize())


def delete_record():
    doc = get_record()
    if doc:
        print('')
        for k,v in doc.items():
            if k != '_id':
                print(k.capitalize() + ': ' + v.capitalize())

        print('')
        confirmation = input('Is this the record you want to delete ?\nY or N > ')
        print('')

        if confirmation.lower() == 'y':
            try:
                coll.remove(doc)
                print('Record deleted!')
            except:
                print('Error accessing the database')
        else:
            print('document not deleted')


def edit_record():
    doc = get_record()
    if doc:
        update_doc = {}
        print('')
        for k,v in doc.items():
            if k != '_id':
                update_doc[k] = input(k.capitalize() + "[" + v + "] > ")

                if update_doc[k] =='':
                    update_doc[k] = v
        try:
            coll.update_one(doc, {'$set': update_doc})
            print('')
            print('Document updated')
            print(doc)
        except:
            print("Error accessing the database")

def main_loop():
    while True:
        option = show_menu()
        if option == '1':
            add_record()
        elif option == '2':
            find_record()
        elif option == '3':
            edit_record()
        elif option == '4':
            delete_record()
        elif option == '5':
            check_all()
        elif option == '6':
            conn.close()
            break
        else:
            print('Invalid option')
        print('')


conn = mongo_connect(MONGO_URI)
coll = conn[DATABASE][COLLECTION]
main_loop()
