# Write a class “Calculator” capable of finding square, cube and square root of a number.

class Calculator:

    def __init__(self, number):
        self.number = number

    def square(self):
        return self.number ** 2

    def cube(self):
        return self.number ** 3

    def root(self):
        return self.number ** 0.5

# Example usage
calc = Calculator(4)
ans = calc.square()
print(f'Square root is {ans}')
ans1 = calc.cube()
print(f'Cube is {ans1}')
ans2 = calc.root()
print(f'Root is {ans2}')