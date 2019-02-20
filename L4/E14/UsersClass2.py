import csv

def yes_or_no(question):
    while "the answer is invalid":
        reply = str( input(question+' (y/n): ')).lower().strip()
        if reply[:1] == 'y':
            return True
        if reply[:1] == 'n':
            return False
        
class User(object):
    def __init__(self, name, address, phone, email):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
    def saveAllRecord(object):
        print("hello")
        with open('userlist.txt','w') as f:
            f.write(user.name).splitlines()



t = [user.name,user.address,user.phone,user.email]
