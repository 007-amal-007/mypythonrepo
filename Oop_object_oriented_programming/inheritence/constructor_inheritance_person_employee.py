class Person:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
    def print(self):
        print(self.name,self.age,self.address)
class Employee(Person):
    def __init__(self,id,salary,name,age,address):
        super().__init__(name,age,address)
        self.id=id
        self.salary=salary
    def printv(self):
        print(self.id)
        print(self.salary)
        print(self.name)
        print(self.age)
        print(self.address)

emp=Employee(1,50000,"sifla",23,"trgbkfbiurgfuodoeu")
emp.print()
emp.printv()