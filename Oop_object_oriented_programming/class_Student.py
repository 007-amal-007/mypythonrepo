class Student:
    def setvalue(self,school_name,roll_no,name,clas):
        self.school_name=school_name
        self.roll_no=roll_no
        self.name=name
        self.clas=clas
    def printvalue(self):
        print("school name=",self.school_name,"\n","roll no:",self.roll_no,"\n","name=",self.name,"\n","class=",self.clas)
ref=Student()
ref.setvalue("PTMHSS.TKD",12,"SIFLA","10.N")
ref.printvalue()
