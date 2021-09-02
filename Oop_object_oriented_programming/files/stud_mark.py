class Student:
    def __init__(self,name,rollno,course,mark):
        self.name=name
        self.rollno=rollno
        self.course=course
        self.mark=mark
    def printval(self):
        print("name:",self.name)
        print("roll no:",self.rollno)
        print("course:",self.course)
        print("mark:",self.mark)
    def __str__(self):
        return self.rollno
f1=open("stud",'r')
for line in f1:
    l=line.split(",")
    name=l[0]
    rollno=l[1]
    course=l[2]
    mark=l[3]
    std=Student(name,rollno,course,mark)
    # print(std)
    if std[3] ==200:
        std.printval()
