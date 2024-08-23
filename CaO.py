# in class you can define your own data types- it is an overview of what a certain data type is
# object is the actual data type with info
# object is an instance of a class

class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
