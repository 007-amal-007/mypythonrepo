#multi level inheritance / heirarchical inheritance
class A:
    def printA(self):
        print("inside A")
class B(A):
    def printB(self):
        print("inside B")
class C(B):
    def printC(self):
        print("inside C")

a=A()
a.printA()

b=B()
b.printB()
b.printA()

c=C()
c.printC()
c.printB()
c.printA()