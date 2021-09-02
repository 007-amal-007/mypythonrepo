class Person:
    def set(self,name,age,address):
        self.name=name
        self.age=age
        self.adress=address
        print(self.name,self.age,self.adress)
class Parent:
    def setv(self,child_name,job):
        self.child_name=child_name
        self.job=job
        print(self.child_name,self.job)
class Employee(Person,Parent):
    def setvalue(self,id,salary,dept):
        self.id=id
        self.salary=salary
        self.dept=dept
        print(self.id,self.salary,self.dept)

emp=Employee()
emp.set("ramu",23,"oihgureihfyewtrgfdbgeuygf")
emp.setv("rahul","teacher")
emp.setvalue("klmn",23000,"cs")
