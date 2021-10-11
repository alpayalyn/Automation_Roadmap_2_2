class Person():

    def __init__(self, name, surname, age, country, city, skill_list):

        self.name = name
        self.surname = surname
        self.age = age
        self.country = country
        self.city = city
        self.skill_list = skill_list

    def add_Skills(self):

        yetenek = input("Which skill you want to add?")
        self.skill_list.append(yetenek)
        print(self.skill_list)

    def Person_Info(self):

        return self.name, self.surname, self.age, self.country, self.city, self.skill_list

AbouthePerson = Person("Alpay", "Alin", "18", "Turkey", "Istanbul", ["Basketbol"])



while True:

    answer = input("Do you want to add skill into the skills list? Y / N")

    if(answer == "Y"):

        AbouthePerson.add_Skills()

        lelo = AbouthePerson.Person_Info()
        print(lelo)


    else:

        lelo = AbouthePerson.Person_Info()
        print(lelo)

        break

