class Animal:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def eat(self):
        print("Animal eats")


class Dog(Animal):

    def bark(self):
        print("Dog barks")

dog=Dog("Buddy", "brown")
dog.eat()
print("Dog name:", dog.name)