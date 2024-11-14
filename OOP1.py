# Method Overrding

class Animal:
    name = ""

    def eat(self):
        print("I can EATT")

# Inherit from animal class

class Zebra(Animal):
    # override eat() method

    def eat(self):
        print("Zebras eat grass")

# creating an obj of sub class
Zebra = Zebra()
Zebra.eat()  # Output: Zebras eat grass