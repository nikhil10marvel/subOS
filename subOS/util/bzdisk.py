import threading
import os
import zipfile
import imp


class BZDisk(threading.Thread):

    def __init__(self):
        if not os.path.exists('./disk/'):
            os.mkdir('./disk/')
        threading.Thread.__init__(self)
        if not os.path.exists('./drive1.disk'):
            self.first_boot = True
        self.zip = zipfile.ZipFile('drive.disk', 'w')
        self.init_dir = os.getcwd()
        self.users_man = imp.load_source('users_man', './users_man.py')

    def save_disk(self):
        self.zip_dir(self.init_dir+'/disk/', self.zip)

    def zip_dir(self , path, zipfile):
        # ziph is zipfile handle
        for root, dirs, files in os.walk(path):
            for file in files:
                zipfile.write(os.path.join(root, file))

    def run(self):
        if self.first_boot:
            print("Welcome to subOS first boot program")
            print("This program will take you through the first boot install")
            user = raw_input('Please Enter administrator user name:')
            passw1 = raw_input('Enter password ')
            passw2 = raw_input('Confirm password ')
            if passw1 == passw2:
                users_man.UsersManager()


disk = BZDisk()
disk.start()
