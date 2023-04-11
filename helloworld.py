
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.occupation = []

    def Occupation(self, occupant):
        self.occupation.append(occupant)

person1 = Person("Ola", 21, "male")
person1.Occupation("Tailor")

person2 = Person("james", 22, "male")
person2.Occupation("students")




print(f'Hello, my name is {person1.name} I am {person1.age} years old. I am a {person1.gender} and I work as a {"".join(person1.occupation)}\n')
print(f'Hello, my name is {person2.name} I am {person2.age} years old. I am a {person2.gender} and I work as a {"".join(person2.occupation)}')


