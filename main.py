#практика
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Student(Person):
    def __init__(self, name, age, gender, __student_id):
        super().__init__(name, age, gender)
        self.__student_id = __student_id

    def get_student_id(self):
        return self.__student_id

    def display_subject(self, subjects):
        print(f"Студент {self.name} вивчив такі предмети: ")
        for subject in subjects:
            print(subject)

class Teacher(Person):
    def __init__(self, name, age, gender, employee_id):
        super().__init__(name, age, gender)
        self.employee_id = employee_id

student1 = Student("Oleg", 15, "male", 34344)
student2 = Student("Olga", 16, "female", 342435)
print(f"Студент на ім'я {student1.name} з id:{student1.get_student_id()}")
student1.display_subject(['Math', 'Science', "History"])
