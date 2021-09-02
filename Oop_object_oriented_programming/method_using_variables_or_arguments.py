#class
class Person:
    def setvalue(self,name,age):
        self.name=name
        self.age=age
    def printvalue(self):
        print("name=",self.name)
        print("age=",self.age)
#object
ref=Person()
ref.setvalue("anu",23)
ref.printvalue()