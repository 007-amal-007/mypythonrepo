class Student:
    def show(self,mark,clas):
        self.mark=mark
        self.clas=clas
        print(self.clas,self.mark)
class Teacher(Student):
    def show(self,name,id,dept,sub):
        self.name=name
        self.id=id
        self.dept=dept
        self.sub=sub
        print(self.name,self.id,self.dept,self.sub,self.mark,self.clas)
stud=Student()
# stud.show("manu",2,"cs","java",56,"bca")
stud.show(56,"bca")



