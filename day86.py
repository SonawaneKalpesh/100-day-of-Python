class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


animal = Animal()
dog = Dog()
cat = Cat()

animal.sound()
dog.sound()
cat.sound()