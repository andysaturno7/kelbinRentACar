from user import User
from db import db

class Authentication:
    def signIn(self, username, password):
        signed = False
        for _user in db['users']:
            if(_user['username'] == username and _user['password'] == password):
                signed = User(_user)
                break
        return signed


    