class Contestant:
   
    diction = dict() 

    def __init__(self, name, nationalId, sex, score = 0):
        self.nationalId = nationalId
        self.diction[nationalId] = {"name":name, "sex":sex ,"score":score}
    
    def increase_score(self, amount):
        Id = self.nationalId
        if Id in self.diction:
            self.diction[Id]["score"] += amount

    def decrease_score(self, amount):
        Id = self.nationalId
        if Id in self.diction:
            self.diction[Id]["score"] -= amount

    def show_score(self):
        Id = self.nationalId
        print(self.diction[Id]["score"])

    def withdraw(self):
        Id = self.nationalId
        name = self.diction[Id]["name"]
        msg = " -{} with the NationalId : {}, withdrew from the competition"
        print(msg.format(name, Id))
        del self.diction[Id]
        
class Classification:

    listx = list()

    def __init__(self, diction = {}):
        self.diction = Contestant.diction
        # add items from dict to list
        for key in self.diction:
            self.listx.append(self.diction[key])
        # sort by score
        for j in range(len(self.listx)):
            for i in range(len(self.listx)-1):
                if self.listx[i]["score"] < self.listx[i+1]["score"]:
                    self.listx[i], self.listx[i+1] = self.listx[i+1], self.listx[i]

    def table(self):
        counter = 1
        for i in range(len(self.listx)):
            name = self.listx[i]["name"]
            score = self.listx[i]["score"]
            print("{}-> {}\t{}".format(counter, name, score))
            counter += 1

    def gentlemans_table(self):
        counter = 1
        for i in range(len(self.listx)):
            if self.listx[i]["sex"] == "male":
                name = self.listx[i]["name"]
                score = self.listx[i]["score"]
                print("{}-> {}\t{}".format(counter, name, score))
                counter += 1

    def ladies_table(self):
        counter = 1
        for i in range(len(self.listx)):
            if self.listx[i]["sex"] == "female":
                name = self.listx[i]["name"]
                score = self.listx[i]["score"]
                print("{}-> {}\t{}".format(counter, name, score))
                counter += 1
