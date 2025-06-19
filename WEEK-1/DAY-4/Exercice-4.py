class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
        return self.age >= 18


class Family:
    def __init__(self, last_name, members=None):
        self.last_name = last_name
        self.members = members if members is not None else []

    def born(self, first_name, age):
        new_person = Person(first_name, age)
        new_person.last_name = self.last_name
        self.members.append(new_person)

    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print(f"You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print(f"Sorry, you are not allowed to go out with your friends.")
                return
        print(f"No member named {first_name} was found.")

    def family_presentation(self):
        print(f"\nFamily Name: {self.last_name}")
        print("Members:")
        for member in self.members:
            print(f"- {member.first_name}, Age: {member.age}")


my_family = Family("Sabil")


my_family.born("Hafssa", 22)
my_family.born("Yasmine", 15)
my_family.born("Adam", 18)


my_family.family_presentation()
my_family.check_majority("Hafssa")
my_family.check_majority("Yasmine")  
my_family.check_majority("Adam")     
my_family.check_majority("Sara")    