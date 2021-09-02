class Parent:
    def __init__(self,name,job,addres):
        self.name=name
        self.job=job
        self.addres=addres
    def printv(self):
        print("\n","name:",self.name,"\n","job:",self.job,"\n","adress:",self.addres)
class Teacher(Parent):
    collage="MES Kalladi Collage MKD"
    def __init__(self,teach_name,id,dept,sub,name,job,addres):
        super().__init__(name,job,addres)
        self.teach_name=teach_name
        self.id=id
        self.dept=dept
        self.sub=sub
    def printvalue(self):
        print("\n",self.teach_name,"\n","id:",self.id,"\n","department:",self.dept,"\n","subject:",self.sub,"\n",Teacher.collage)
    def __str__(self):
        return str(self.id)+" "+self.teach_name
te=Teacher("musthaq",1,"CS","java","noor","electrical engineer","pp tkd")
print(te)
te.printvalue()
te.printv()

teach=Teacher("surayya",2,"CS","COA","sifla","software engineer","gheirhgoes;i")
teach.printvalue   ()
teach.printv()
