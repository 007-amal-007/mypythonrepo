#overriding : same method name
#             same num of arguments
#child class method override parent class method .
#work latest method
class Peron:
    def printval(self,name):
        self.name=name
        print("inside person method,",self.name)
class Child(Peron):
    def printval(self,class1):
        self.class1=class1
        print("inside child method,",self.class1)
    def __str__(self):
        return self.class1
ch=Child()
ch.printval("abc")
ch.printval("child")
print(ch)