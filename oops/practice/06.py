# Create a class ‘Employee’ and add salary and increment properties to it. Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter which changes the value of increment based on the salary.

class Employee:
    salary = 100
    increment = 10  # Default increment of 10%
    @property
    def afterIncrement(self):
        return self.salary + self.salary * (self.increment / 100)

s = Employee()
print(s.afterIncrement)