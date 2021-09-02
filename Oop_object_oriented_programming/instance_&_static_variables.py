# types of variables:
# 1)instance variables = define inside a method / related to method
#     it can be accessed by using self.  / related to class
# 2)static variables = define inside a class
#     it can be accessed by using class name
#         print(Student.school)


class Student:
    school="PTMHSS.TKD"     #STATIC_VARIABLE
    def setvalue(self,roll_no,name,clas):
        self.roll_no=roll_no
        self.name=name
        self.clas=clas
    def printvalue(self):
        print("\n","school=",Student.school,"\n","roll no:",self.roll_no,"\n","name=",self.name,"\n","class=",self.clas)
ref=Student()
ref.setvalue(12,"SIFLA","10.N")
ref.printvalue()

re=Student()
re.setvalue(11,"sherin",)

