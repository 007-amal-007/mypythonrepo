class Person:
    def set(self,name,age,job,address):
        self.name=name
        self.age=age
        self.job=job
        self.address=address
        print(self.name,self.age,self.job,self.address)
class Parent:
    def setv(self,child_name,mark,clas):
        self.child_name=child_name
        self.mark=mark
        self.clas=clas
        print(self.child_name,self.mark,self.clas)
class Teacher(Person,Parent):
    def setvalue(self,name,sub,dept):
        self.name=name
        self.sub=sub
        self.dept=dept
        print(self.name,self.sub,self.dept)

ref=Teacher()
ref.setvalue("musthaq","java","CS")
ref.set("mohammed",45,"sales_man","pptkderf")
ref.setv("sifla","85%","BCA")
