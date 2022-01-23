class Contestant:
   
    diction = {}

    def __init__(self, name, nationalId, sex, score = 0):
        self.nationalId = nationalId
        self.diction[self.nationalId] = {"name":name, "sex":sex ,"score":score}
    
    def increase_score(self, amount):
        if self.nationalId in self.diction:
            self.diction[self.nationalId]["score"] += amount

    def decrease_score(self, amount):
        if self.nationalId in self.diction:
            self.diction[self.nationalId]["score"] -= amount

    def show_score(self):
        print(self.diction[self.nationalId]["score"])

    def withdraw(self):
        Id = self.nationalId
        msg = " Participant \"%s\" with the NationalId:%d, withdrew from the competition"
        print(msg %(self.diction[Id]["name"], Id))
        del self.diction[Id]
        
class Classification:

    listx = []

    def __init__(self, diction = {}):
        self.diction = Contestant.diction
        for key in self.diction:
            self.listx.append(self.diction[key])
        for j in range(len(self.listx)):
            for i in range(len(self.listx)-1):
                if self.listx[i]["score"] < self.listx[i+1]["score"]:
                    self.listx[i], self.listx[i+1] = self.listx[i+1], self.listx[i]

    def table(self):
        counter = 1
        for i in range(len(self.listx)):
            name = self.listx[i]["name"]
            score = self.listx[i]["score"]
            print(f"{counter}-> {name}\t{score}")
            counter += 1

    def gentlemans_table(self):
        counter = 1
        for i in range(len(self.listx)):
            if self.listx[i]["sex"] == "male":
                name = self.listx[i]["name"]
                score = self.listx[i]["score"]
                print(f"{counter}-> {name}\t{score}")
                counter += 1

    def ladies_table(self):
        counter = 1
        for i in range(len(self.listx)):
            if self.listx[i]["sex"] == "female":
                name = self.listx[i]["name"]
                score = self.listx[i]["score"]
                print(f"{counter}-> {name}\t{score}")
                counter += 1

arya = Contestant("Arya", 991771231, "male")
amir = Contestant("Amir", 991771233, "male")
parsa = Contestant("Parsa", 991771227, "male")
aysa = Contestant("Aysa", 991772026, "female")

arya.show_score()
amir.withdraw()
aysa.increase_score(25)
aysa.show_score()
parsa.decrease_score(10)
parsa.show_score()



c = Classification()
c.table()
c.gentlemans_table()

