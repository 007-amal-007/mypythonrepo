#constructure used to initilize instance variables
class Person:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address

    def printvalue(self):
        print(self.name,self.age,self.address)
obj=Person("anu",26,"abc")
obj.printvalue()