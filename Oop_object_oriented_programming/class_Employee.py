class Employee:
    def setvalue(self,id,name,salary,company_name,department):
        self.id=id
        self.name=name
        self.salary=salary
        self.company_name=company_name
        self.department=department
    def printvalue(self):
        print("id=",self.id)
        print("name=",self.name)
        print("salary=",self.salary)
        print("company_name=",self.company_name)
        print("department=",self.department)
ref=Employee()
ref.setvalue(1,"anu",23000,"infosys","IT")
ref.printvalue()

re=Employee()
re.setvalue(2,"minu",22000,"exelson","database")
re.printvalue()
