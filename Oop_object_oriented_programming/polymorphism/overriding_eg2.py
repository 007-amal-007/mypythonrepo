# class Student:
#     def show(self,mark,class1):
#         self.mark=mark
#         self.class1=class1
#         print(self.mark,self.class1)
#     def show(self,name,address):
#         self.name=name
#         self.address=address
#         print(self.name,self.address)
# stud=Student()
# stud.show("sifla","bca")

class Student:
    def show(self,mark,class1):
        self.mark=mark
        self.class1=class1
        print(self.mark,self.class1)
class Teacher(Student):
    def show(self,name,address):
        self.name=name
        self.address=address
        print("child class method override parent class method or print latest method...")
        print(self.name,self.address)
teach=Teacher()
teach.show("sifla","pp tkd")