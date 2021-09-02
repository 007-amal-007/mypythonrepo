class Person:
    def setvalue(self,name,place):
        self.name=name
        self.place=place
        print(self.name)
        print(self.place)
class Employee(Person):
    def set(self,id,salary):
        self.id=id
        self.salary=salary
        print(self.id)
        print(self.salary)

# per=Person()
# per.setvalue("sifla","tkd")

emp=Employee()
emp.setvalue("anu","mkd",)
emp.set(2,22000)


