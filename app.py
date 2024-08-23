# module is any external file with essential functions that you can use in another file
# they save on time
# pip is a package manager that helps install,manage,update and uninstall modules

import useful_tools

print(useful_tools.roll_dice(10))

from CaO import Student

student1 = Student("Dan", "Computer Science", 3.2, False)

print(student1.gpa)
