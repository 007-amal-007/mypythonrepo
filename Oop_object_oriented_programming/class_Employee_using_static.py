class Employee:
    company_name="luminar"
    def setvalue(self,id,name,department):
        self.id=id
        self.name=name
        self.department=department
    def printvalue(self):
        print("\n",self.id,"\n",self.name,"\n",self.department,"\n",Employee.company_name)
ref=Employee()
ref.setvalue(1,"anu","developers")
ref.printvalue()

em=Employee()
em.setvalue(2,"minu","back_end developers")
em.printvalue()