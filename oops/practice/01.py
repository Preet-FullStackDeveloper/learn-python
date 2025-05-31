# Create a class “Programmer” for storing information of few programmers working at Microsoft.
class Programmer:
    def __init__(self, name, age):
        self.name = name
        self.age = age


employer = Programmer('John', 18)
print(employer.name)
print(employer.age)
