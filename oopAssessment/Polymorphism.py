class Cat:
    def make_sound(self):
        print("Meow")

class Dog:
    def make_sound(self):
        print("Woof")

def animal_sound(animal):
    animal.make_sound()

animal_sound(Cat())
animal_sound(Dog())