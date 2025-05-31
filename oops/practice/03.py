# Add a static method in problem 2, to greet the user with hello.

class Calculator:

    def __init__(self, number):
        self.number = number

    def square(self):
        print(f'Calculating square of {self.number} is {self.number ** 2}')

    def cube(self):
        print(f'Calculating cube of {self.number} is {self.number ** 3}')

    def root(self):
        print(f'Calculating root of {self.number} is {self.number ** 0.5}')

    @staticmethod
    def greet():
        print('Hello, welcome to the Calculator!')

# Example usage
calc = Calculator(4)
calc.greet()
calc.square()
calc.cube()
calc.root()
