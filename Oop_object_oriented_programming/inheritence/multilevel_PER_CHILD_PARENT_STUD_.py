# child parent class....person inherit
# student class....child

class Person:
    def per(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class Child(Person):
    def ch(self,clas,school):
        self.clas=clas
        self.school=school
        print(self.clas,self.school)
class Parent(Person):
    def par(self,job,address):
        self.job=job
        self.address=address
        print(self.job,self.address)
class Student(Child):
    def stud(self,mark):
        self.mark=mark
        print(self.mark)
        print(self.mark)
a=Person()
a.per("sifla",23)

b=Child()
b.ch(10,"mes")
b.per("manu",34)

c=Parent()
c.par("sales","erftghejhgfyegf")
c.per("nooru",26)

d=Student()
d.ch(8,"ptm")
d.stud("87%")