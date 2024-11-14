# MultiLevel Inheritence 

class SuperClass:
    def super_method(self):
        print("This is a method from SuperClass")

class DerivedClass1(SuperClass):
    def derived_method1(self):
        print("Derived class 1 method")

class DerivedClass2(DerivedClass1):
    def derived_method2(self):
        print("Derived class 2 method called")

# Creating an obj of Derived Class 2

d2 = DerivedClass2()
d2.super_method()
d2.derived_method1()
d2.derived_method2()