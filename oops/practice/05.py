# Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’.


class Animals:
    def __init__(self):
        self.type = "Animal"
        print(f'{self.type} class initialized.')


class Pets(Animals):
    def __init__(self):
        super().__init__()
        self.type = "Pet"
        print(f'{self.type} class initialized.')

class Dog(Pets):
    @staticmethod
    def bark():
        print("Woof! Woof!")