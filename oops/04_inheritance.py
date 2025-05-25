# Inheritance in Python

## Parent class
class Employee:
    def showEmployee(self):
        print("This is the Employee class")

# Child class inheriting from Employee
class Manager():
    def show(self):
        print("This is the Manager class")
        
#Multilevel inheritance example
class Resource(Manager):
    def showResource(self):
        print("This is the Resource class")
'''      
x = Resource()
x.show()  # Output: This is the Manager class
x.showEmployee()  # Output: This is the Employee class
x.showResource()  # Output: This is the Resource class

print('------------------------------')
'''     
#Multiple inheritance example
class Developer(Employee, Manager):
    def showDeveloper(self):
        print("This is the Developer class")

d = Developer()
d.showEmployee()  # Output: This is the Employee class
d.show()  # Output: This is the Manager class
d.showDeveloper()  # Output: This is the Developer class
        