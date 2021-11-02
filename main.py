class Person():
    def __init__(self, name = "ALpay", surname = "Alin", age = 24, country = "Turkey", city = "Istanbul", skillList = ["Basketbol"]):
        self.name = name
        self.surname = surname
        self.age = age
        self.country = country
        self.city = city
        self.skillList = skillList

    def addSkills(self):
        skill = input("Which skill you want to add?")
        self.skillList.append(skill)
        print(self.skillList)

    def personInformation(self):
        return self.name, self.surname, self.age, self.country, self.city, self.skillList

aboutPerson = Person()

while True:
    answer = input("Do you want to add skill into the skills list? Y / N")

    if(answer == "Y"):
        aboutPerson.addSkills()
        print(aboutPerson.personInformation())

    else:
        aboutPerson.personInformation()
        break