# Small login/register demo that persists users to a JSON file instead of a real database.
#
# This is a toy example of "persistence": normally the list of registered
# users would live in a database, but here we simulate that by saving the
# user list to a plain JSON file (users.json) on disk, so the accounts
# survive between separate runs of the script.
import json
import os

class User:
    def __init__(self, username, password, email):
        # NOTE: storing the password as plain text (not hashed) is only
        # acceptable because this is a learning exercise - a real
        # application must never store passwords this way.
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    def __init__(self):
        self.users = []          # in-memory list of User objects
        self.isLoggedIn = False
        self.currentUser = {}

        # load users from .json file
        self.loadUsers()

    def loadUsers(self):
        # os.path.exists(path) checks whether the file is actually there
        # before trying to open it, avoiding a crash on the very first run
        # (when no users have been registered/saved yet).
        if os.path.exists('users.json'):
            # Opening with "with" guarantees the file gets closed
            # automatically afterwards, even if an error happens inside the
            # block. encoding='utf-8' makes sure non-ASCII characters (like
            # accented letters in an email or name) are read correctly.
            with open('users.json','r',encoding='utf-8') as file:
                # json.load(file) parses the JSON stored in the file. Here
                # the file's top-level JSON value is a LIST OF STRINGS -
                # each string itself being a separate small JSON object
                # (see savetoFile() below for why it was saved that way) -
                # so a second json.loads() per item is needed to turn each
                # of those strings into an actual dict.
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    newUser = User(username = user['username'], password = user['password'], email = user['email'])
                    self.users.append(newUser)
            print(self.users)

    def register(self, user: User):
        # "user: User" is a type hint - it documents that this parameter is
        # expected to be a User instance. Python doesn't enforce this at
        # runtime; it's purely there to help readers (and some editors/tools).
        self.users.append(user)
        self.savetoFile()
        print('User created.')

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print('Logged in.')
                break

    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print('Logged out.')

    def identity(self):
        if self.isLoggedIn:
            print(f'username: {self.currentUser.username}')
        else:
            print('Not logged in.')

    def savetoFile(self):
        encoded_users = []

        for user in self.users:
            # user.__dict__ gives you the object's attributes as a plain
            # dict, e.g. {"username": "...", "password": "...", "email": "..."}
            # - a handy trick for turning a simple object into something
            # json.dumps() can serialize directly. Each user is converted to
            # its OWN JSON string here (rather than json-encoding the whole
            # list of dicts at once), which is why loadUsers() above has to
            # call json.loads() a second time per entry to unpack them again.
            encoded_users.append(json.dumps(user.__dict__))

        with open('users.json','w') as file:
            # This writes a JSON array of strings, e.g. ["{...}", "{...}"] -
            # a list where each element is itself JSON-encoded text.
            json.dump(encoded_users, file)


repository = UserRepository()

while True:
    # .center(50,'*') pads the string with '*' characters on both sides
    # until it's 50 characters wide, centering "Menu" in the middle - a
    # simple way to print a decorative header.
    print('Menu'.center(50,'*'))
    choice = input('1- Register\n2- Login\n3- Logout\n4- identity\n5- Exit\nyour choice: ')
    if choice == '5':
        break
    else:
        if choice == '1':
            username = input('username: ')
            password = input('password: ')
            email = input('email: ')

            user = User(username=username, password = password, email = email)
            repository.register(user)
        elif choice == '2':
            if repository.isLoggedIn:
                print('You are already logged in')
            else:
                username = input('username: ')
                password = input('password: ')
                repository.login(username, password)
        elif choice == '3':
            repository.logout()
        elif choice == '4':
            repository.identity()
        else:
            print('invalid choice')
