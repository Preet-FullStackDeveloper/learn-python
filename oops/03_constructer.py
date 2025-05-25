class Employee:
    language = "Python"
    salary = 100000
    
    def __init__(self, name, age): #Dunder method to initialize the object. all underscore methods are called dunder methods
        self.name = name
        self.age = age
        print("Employee object created")
        
    def getInfo(self):
        print(f"Language: {self.language}, Salary: {self.salary}, name: {self.name}, age: {self.age}")
        
    #Using a static method to greet
    @staticmethod
    def greet():
        print("Hello, welcome to the company!")
# Create an instance of Employee
John = Employee('John Doe', 30)
John = Employee('John Doe', 31)
John.getInfo()  # Call the method using the instance