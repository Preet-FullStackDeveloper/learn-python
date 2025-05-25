class Employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"This is the Employee class with a static variable a = {cls.a}")

x = Employee()
x.a = 2  # Changing the static variable a
x.show()  # Output: This is the Employee class with a static variable a = 2