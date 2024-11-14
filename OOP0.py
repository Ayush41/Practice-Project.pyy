# Inheritence in pyhton

class Person(object):
    # Constructor
    def __init__(self,name):
        self.name = name
    # Get Name 
    def getName(self):
        return self.name
    
    # To check if this person is an emp
    def isEmp(self):
        return False

# Inherited from person class
class Employee(Person):
    def isEmp(self):
        return True
    
# Main Code

emp = Person("Itachi")
print(emp.getName(),emp.isEmp())

emp = Employee("Naruto")
print(emp.getName(),emp.isEmp())
