#two string method
class Vehicle:
    def __init__(self,model,regno,clr):
        self.model=model
        self.regno=regno
        self.clr=clr
    def print(self):
        print(self.model)
        print(self.regno)
        print(self.clr)
    #2 string method
    #can only pass string
    #can onl pass a single value,if we want to add 2 values use  "+"
    def __str__(self):
        return self.model+self.clr
veh=Vehicle("BMW","KL-10 1516","BLUE")
veh.print()
print(veh)