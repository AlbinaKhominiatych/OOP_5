#успадкування
class Animal:
    def sound(self):
        print("Гучно оре")
class Dog(Animal):
    def sound(self):
        Animal.sound(self)
        print("Гавкати")
dog = Dog()
dog.sound()