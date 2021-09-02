class Teacher:
    clg_name="MES.KALLADI.CLG.MKD"
    def __init__(self,name,id,sub):
        self.name=name
        self.id=id
        self.sub=sub
    def printvalue(self):
        print("\n","name=",self.name,"\n","id=",self.id,"\n","subject=",self.sub,"\n","collage name=",Teacher.clg_name)
ref=Teacher("MEENAKSHI","KIARBCA010","MALAYALAM")
ref.printvalue()

obj=Teacher("anu",2,"maths")
obj.printvalue()