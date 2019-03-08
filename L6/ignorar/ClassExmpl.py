

class Student:
    def __init__ (self, fname, age, year):
        self.name = fname
        self.age = age
        self.year = year

    def last_name(self):
        return self.name.split(' ')[1]

stud1 = Student( 'Jake Miller', 17, 'Senior')
stud2 = Student('Alice Carry', 16, 'junior')
stud3 = Student()

# def set_info(student, fname, age, year):
#     student.name = fname
#     student.age = age
#     student.year = year

# stud1.set_info( 'Jake Miller', 17, 'Senior')
# stud2.set_info('Alice Carry', 16, 'junior')


# Student.last_name(stud1)
# stud1.last_name()

# stud1.name = 'Jake Miller'
# stud1.age = 17
# stud1.year = 'Senior'
#
# stud2.name = 'Alice Carry'
# stud2.age = 16
# stud2.year = 'Junior'
#

print(stud2.name)
