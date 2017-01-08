import ConfigParser
import os
import threading


class UsersManager(threading.Thread):

    def __init__(self):
        self.parser = ConfigParser.ConfigParser()
        self.parser.readfp(open('users.cfg' , 'r+'))

    def makeadmuser(self, user, password):
        self.parser.add_section('Admin')
        self.parser.set('Admin', 'username', user)
        self.parser.set('Admin', 'password', password)

    def makedefuser(self, user, password):
        self.parser.add_section('Others')
        self.parser.set('Admin', 'username', user)
        self.parser.set('Admin', 'password', password)

    def save(self):
        with open('users.cfg', 'r+') as file:
            self.parser.write(file)
