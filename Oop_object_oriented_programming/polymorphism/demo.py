# polymorphism: (manyforms)
#overloading : same method name
#              diff num of parameters
#work the latest method

#overriding : same method name
#             same num of arguments

class Person:
    def show(self,num1):
        self.num1=num1
        print(self.num1)
class Student(Person):
    def show(self,num2,num3):
        self.num2=num2
        self.num3=num3
        print(self.num2,self.num3)
stud=Student()
stud.show(3,2)

std=Student()
std.show(3)