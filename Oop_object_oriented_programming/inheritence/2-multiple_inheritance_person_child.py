#multiple_inheritance

class Person:
    def setvalue(self,name,age,job,addres):
        self.name=name
        self.age=age
        self.addres=addres
        self.job=job
        print(self.name,self.age,self.job,self.addres)

class Child:
    def setv(self,std,school):
        self.std=std
        self.school=school
        print(self.std,self.school)

class Student(Person,Child):
    def set(self,roll_no,mark):
        self.roll_no=roll_no
        self.mark=mark
        print(self.roll_no,self.mark)

st=Student()
st.setvalue("anu",21,"teacher","abc")
st.setv(4,"ptmhss")
st.set(1,"52%")

#Student....parent==Person,Child