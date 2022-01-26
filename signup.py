class check:
    def __init__(self, kwargs):
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

txt = input()
strip = ["(", ")", "=", "'", ","]
for case in strip:
    txt = txt.replace(case, " ")
txt = txt.split()

diction = {}
for i in range(0, len(txt), 2):
    diction[txt[i]] = txt[i+1]
    
ch = check(diction)
ch.check_registration_rules()
