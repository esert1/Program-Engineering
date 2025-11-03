class Animal:
    def speak(self):
        print("Животное издает звук")

class Dog(Animal):
    def speak(self):
        print("Собака лает")

class Cat(Animal):
    def speak(self):
        print("Кошка мяукает")

animals = [Dog(), Cat(), Animal()]
for a in animals:
    a.speak()
