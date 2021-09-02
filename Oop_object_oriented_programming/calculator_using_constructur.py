# class Calc:
#     print("operations")
#     print("1.add")
#     print("2.subtract")
#     print("3.mutiplication")
#     print("4.division")
#     def add(self,a,b):
#         self.a=a
#         self.b=b
#         print("sum=",self.a+self.b)
#     def sub(self,a,b):
#         self.a = a
#         self.b = b
#         print("subtraction=",self.a-self.b)
#     def mul(self,a,b):
#         self.a = a
#         self.b = b
#         print("multiplication=",self.a*self.b)
#     def div(self,a,b):
#         self.a = a
#         self.b = b
#         print("division=",self.a/self.b)
# while True:
#     choice=int(input("select an operation:"))
#     a=int(input("enter first:"))
#     b=int(input("enter second:"))
#     ref=Calc()
#     if choice==1:
#         ref.add(a,b)
#     elif choice==2:
#         ref.sub(a,b)
#     elif choice==3:
#         ref.mul(a,b)
#     elif choice==4:
#         ref.div(a,b)
#     else:
#         print("invalid")




class Calc:
    print("operations")
    print("1.add")
    print("2.subtract")
    print("3.mutiplication")
    print("4.division")
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print("sum=",self.a+self.b)
    def sub(self):
        print("subtraction=",self.a-self.b)
    def mul(self):
        print("multiplication=",self.a*self.b)
    def div(self):
        print("division=",self.a/self.b)

while True:
    choice = int(input("select an operation:"))
    a = int(input("enter"))
    b = int(input("enter"))
    ref = Calc(a, b)
    if choice == 1:
        ref.add()
    elif choice==2:
        ref.sub()
    elif choice==3:
        ref.mul()
    elif choice==4:
        ref.div()
    else:
        print("invalid")














