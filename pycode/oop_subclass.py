class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Initialize SchoolMember :{}'.format(self.name))
    def tell(self):
        print('Name:{} Age:{}'.format(self.name, self.age))

class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
    def tell(self):
        SchoolMember.tell(self)
        print('Salary:{}'.format(self.salary))

class Student(SchoolMember):
    def __init__(self, name, age, score):
        SchoolMember.__init__(self, name, age)
        self.score = score
    def tell(self):
        SchoolMember.tell(self)
        print('Score:{}'.format(self.score))


t = Teacher('MrLin', 18, 98500)
s = Student('Lin', 78, 98)

members = [t, s]
for member in members:
    member.tell()
