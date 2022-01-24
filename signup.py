import re

class check:
    def __init__(self, **kwargs):
        self.kwargs = kwargs 
        
    def check_registration_rules(self):
        validUsers = []
        for username in self.kwargs:
            valid = True
            if len(username) < 4:
                valid = False
                continue
            if username == "python" or username == "quera":
                valid = False
                continue
            if len(self.kwargs[username]) < 6:
                valid = False
                continue
            if self.kwargs[username].isdigit():
                valid = False
                continue
            if valid:
                validUsers.append(username)
       
        counter = len(validUsers)
        print("[", end="")
        for user in validUsers:
            print("'{}'".format(user), end="")
            if counter > 1:
                print(",", end="")
            counter -= 1
        print("]")

print(diction)
ch = check(username="password", sadegh="He3@lsa", python="kLS45@l$")
ch.check_registration_rules()
