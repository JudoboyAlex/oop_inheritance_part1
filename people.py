class Person:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"Hi, my name is {self.name}"

class Student(Person):

    def learn(self):
        return "I get it!"

class Instructor(Person):

    def teach(self):
        return "An object is an instance of a class"

Nadia = Student("Nadia")
Chris = Instructor("Chris")

print(Nadia.introduce())
print(Chris.introduce())
print(Chris.teach())
print(Nadia.learn())
# print(Nadia.teach()) 
# This doesn't work because no inheritation between student and instructor