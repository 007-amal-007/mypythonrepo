class Student:
    collage="MES KALKADI CLG"
    def __init__(self,name,rollno,dept):
        self.name=name
        self.rollno=rollno
        self.dept=dept
    def printv(self):
        print(self.name)
        print(self.rollno)
        print(self.dept)
        print(Student.collage)
    def __str__(self):
        return self.name+" "+self.dept+" "+str(self.rollno)

stud=Student("sifla",20,"CS")
stud.printv()
print(stud)
std=Student("noor",21,"CS",)
std.printv()
print(std)