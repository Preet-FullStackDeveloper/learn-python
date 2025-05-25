class Employee:
    language = "Python"
    salary = 100000
    
    def getInfo(self):
        print(f"Language: {self.language}, Salary: {self.salary}")
        
    #Using a static method to greet
    @staticmethod
    def greet():
        print("Hello, welcome to the company!")
# Create an instance of Employee
John = Employee()

Employee.getInfo(John)  # Call the method using the instance