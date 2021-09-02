# class Add:
#     def setvalue(self,a,b):
#         self.a=a
#         self.b=b
#     def printvalue(self):
#         print("addition=",self.a+self.b)
# ref=Add()
# ref.setvalue(4,5)
# ref.printvalue()

class Add:
    def set(self,a,b):
        self.a=a
        self.b=b
        print("sum=",self.a+self.b)
ref=Add()
a=int(input("enter"))
b=int(input("enter"))
ref.set(a,b)