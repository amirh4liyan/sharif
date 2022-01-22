class Contestant:
    
    withdrawal = []

    def __init__(self, name, nationalId, sex, score = 0):
        self.name = name
        self.nationalId = nationalId
        self.sex = sex
        self.score = score
    
    def increase_score(self, amount):
        if self.nationalId not in withdrawal:
            self.score += amount

    def decrease_score(self, amount):
        if self.nationalId not in withdrawal:
            self.score -= amount

    def show_score(self):
        print(self.score)

    def withdraw(self):
        self.withdrawal.append(self.nationalId)
        msg = "Participant \"%s\" with the NationalId:%d, withdrew from the competition"
        print(msg %(self.name, self.nationalId))
        
class Classification:
    def __init__(self):
        pass

    def table(self):
        pass

    def gentlemans_table():
        pass

    def ladies_tables():
        pass

arya = Contestant("Arya", 991771231, "male")
amir = Contestant("Amir", 991771233, "male")
parsa = Contestant("Parsa", 991771227, "male")
aysa = Contestant("Aysa", 991772026, "female")

print(arya.withdrawal)

arya.show_score()
amir.withdraw()
aysa.increase_score(25)
aysa.show_score()
parsa.decrease_score(10)
parsa.show_score()



print(arya.withdrawal)
