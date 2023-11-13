#успадкування
class Animal:
    def sound(self):
        print("Гучно оре")
class Dog(Animal):
    pass
dog = Dog()
dog.sound()