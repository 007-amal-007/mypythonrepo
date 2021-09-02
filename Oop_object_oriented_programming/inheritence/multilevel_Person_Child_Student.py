class Person:
    def classp(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class Child(Person):
    def classc(self,std,school):
        self.std=std
        self.school=school
        print(self.std,self.school)
class Student(Child):
    def classs(self,mark):
        self.mark=mark
        print(self.mark)
p=Person()
p.classp("sifa",23)

c=Child()
c.classc("3rd","mes")
c.classp("anu",32)

s=Student()
s.classs("87%")
s.classp("mohammed",47)
s.classc("BCA","MES")
