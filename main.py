#практика
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Student(Person):
    def __init__(self, name, age, gender, student_id):
        super().__init__(self, name, age, gender)
        self.student_id = student_id

class Teacher(Person):
    def __init__(self, name, age, gender, employee_id):
        super().__init__(self, name, age, gender)
        self.employee_id = employee_id