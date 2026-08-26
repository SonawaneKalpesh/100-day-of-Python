class Student:
    def __init__(self, name):
        self.name = name
        print("Object created")

    def __del__(self):
        print("Object destroyed")


student = Student("Rahul")

del student