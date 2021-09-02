class Employee:
    company_name="luminar"
    def __init__(self,id,name,dept):
        self.name=name
        self.id=id
        self.dept=dept
    def printvalue(self):
        print("\n",self.id,"\n",self.name,"\n",self.dept,"\n",Employee.company_name)
ref=Employee(2,"anu","developers")
ref.printvalue()