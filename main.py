class Parent:
    def __init__(self, name):
        self.name = name
        print("Корисна річ")
class Child(Parent):
    def __init__(self, name, additional_info):
        #self.name = name
        super().__init__(name)#виклик конструктора батьківського класу
        self.additional_info = additional_info

child = Child("Oleg", "informaion")
print(child.name, child.additional_info)
