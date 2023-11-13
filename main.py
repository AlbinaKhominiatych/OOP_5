#успадкування
class Animal:
    def sound(self):
        print("Гучно оре")
class Dog(Animal):
    def sound(self):
        super().sound()
        print("Гавкати")
dog = Dog()
dog.sound()