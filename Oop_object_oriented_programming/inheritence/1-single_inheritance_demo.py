#single_inheritance
#class used to inherit is called =super class / parent class / base class .inherit cheyyan use cheythath
#super class used by the class is called = derived class / sub class / child class

class Person:               #super class / parent class / base class
    def walk(self):
        print("person is walking")
    def read(self):
        print("person is reading")
class Student(Person):     #derived class / sub class / child class
    def exam(self):
        print("student attending exams")
per=Person()
per.walk()
per.read()

std=Student()
std.exam()
std.walk()
std.read()

