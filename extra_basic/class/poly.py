class Animal:
    def __init__(self,name):
        self.name = name 

class Dog(Animal):
    def __init__(self,name,legs):
        super().__init__(name)
        self.legs = legs
        