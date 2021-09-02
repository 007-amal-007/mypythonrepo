# 2.eliminate_duplicate
# lst=[1,0,7,5,9,2,3,5,7,2,0,1,10]
# new_list =[]
# [new_list.append(i) for i in lst if i not in new_list]
# print(new_list)


# 3.second_largest
# lst=[3,5,7,9,0,8,55,34,23,76,4,65,12,89,56,76,34,289,49,12,63,976]
# lst.sort()
# print("Second largest element is:", lst[-2])


# #4.common_elements
# a=[1,2,3,45,6,7,33,11,77,9,0,5]
# b=[3,77,0,5,33,6,22,5,90,32,56,78,98,54,67,11,34,88]
# c=[]
# for i in a:
#     if i in b:
#       c.append(i)
# print(c)


#5.calculator
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return  a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b
# def floor_div(a,b):
#     return a//b
# def expo(a,b):
#     return a**b
# print("operations")
# print("1.addition")
# print("2.subtraction")
# print("3.multiplication")
# print("4.division")
# print("5.floor division")
# print("6.exponent")
# while True:
#     choice=int(input("select a operation:"))
#     a=float(input("enter first number:"))
#     b=float(input("enter second number:"))
#     if choice==1:
#         print(add(a,b))
#     elif choice==2:
#         print(sub(a,b))
#     elif choice==3:
#         print(mul(a,b))
#     elif choice==4:
#         print(div(a,b))
#     elif choice==5:
#         print(floor_div(a,b))
#     elif choice==6:
#         print(expo(a,b))
#     else:
#         print("invalid")


#6.prime_numbers(1-50)
# def sum_of_n(min,max):
#     sum=0
#     for a in range(min,max+1):
#         if a>1:
#             for i in range(2,a):
#                 if a%i==0:
#                     break
#             else:
#                 sum=sum+a
#     return (sum)
# print(sum_of_n(1,50))


#7.remove_vowels
# a=input("enter a string:")
# b="aeiou"
# c=""
# for i in a:
#     if i not in b:
#         c=c+i
# print(c)

#8.use_of_functions
# functions are used when we want to use a block  of code repeatedly on a program.
# it reduce memory usage and save our time
# eg:def sum(a,b):
#         return a+b
#    print(sum(2,3))
# functions are 3 types:
# 1.functions with arguments
#     def sum(a,b):
#         print(a+b)
#     sum(2,3)
# 2.functions without arguments
#     def sum()
#         a=3
#         b=2
#         print(a+b)
#     sum()
# 3.functions with arguments and return type
#     the above eg: is for this type

#9.features_of_list_&_set
# set:
#     1.set is "HETEROGENIOUS":we can add different types of elements like string,float,bool in a single set
#     2.set do "NOT KEEP THE ORDER" that we given . arrange elements either in ascending or descending order
#     3.set does not support "DUPLICATION" of elements
#     4.sets are "MUTABLE"
#     5.in set "NESTING NOT POSSIBLE"
# list:
#     1.it "KEEPS ORDER"
#     2.it "SUPPORT DUPLICATION"
#     3.list is "HETEROGENIOUS"
#     4."NESTING IS POSSIBLE"
#     5.lists are "MUTABLE"

#10.list_comprehensions(1-100)
# list comprehensions are used for creating new lists from itarables.
# sometimes we can complete a program with a sigle line of code
# new_list=[i for i in range(1,100+1) if i%5==0]
# print(new_list)

#11.diffrents_b/w_append_&_extend
# extend:
#     when we are trying to add elements of a list to another list separetely we can use extend.add iterable elements
#     eg: list=["hi","hello","bye"]
#         new_list=[1,2,3,4,5]
#         list.extend(new_list)
#         print(list)
# append:
#     append is used when we want to add an element.
#     eg: list=["hi","hello","bye"]
#         list.append(6)
#         print(list)


#1.pattern
#
# 1
# 1 1
# 1 1 1
# 1 1 1 1
# 1 1 1 1 1
# 2 2 2 2 2
# 2 2 2 2
# 2 2 2
# 2 2
# 2
# 3
# 3 3
# 3 3 3
# 3 3 3 3
# 3 3 3 3 3
# 4 4 4 4 4
# 4 4 4 4
# 4 4 4
# 4 4
# 4
# a=int(input("enter initial range:"))
# b=int(input("enter final range:"))
# r=5
# for i in range(a,b):
#     if(i%2==0):
#         for k in range(r,0,-1):
#             for j in range(0,k):
#                 print(i,end=" ")
#             print()
#     else:
#         for l in range(r):
#             for m in range(0,l+1):
#                 print(i,end=" ")
#             print()

#2
# lst=[1,0,7,5,9,2,3,5,7,2,0,1,10]
# print(list(set(lst)))
#


#python advanced section exam
# 5.
# overriding :same method name
#             same num of arguments
# child class method override parent class method .
# in other words ,only work the latest method
# class Book:
#     def printval(self,author_name):
#         self.author_name=author_name
#         print("inside Book method,",self.author_name)
# class fiction(Book):
#     def printval(self,date):
#         self.date=date
#         print("inside fiction method,",self.date)
#     def __str__(self):
#         return self.date
# bk=fiction()
# bk.printval("parent")
# bk.printval("child")
# print(bk)
#
# import re
# f2=open("lum_reg","w")
# rule="([L][U][M]\D{2}[P][Y]{3}$)"
# f=open("valid_reg","r")
# for num in f:
#     number=num.rstrip("\n")
#     matcher=re.fullmatch(rule,number)
#     if matcher !=None:
#         f2.write(number)
#         f2.write("\n")
#
#
# 1.
# class Vehicle:
#     def setval(self,model,color,regno):
#         self.model=model
#         self.color=color
#         self.regno=regno
#         print(self.model,self.color,self.regno)
# class Bus(Vehicle):
#     def setvalue(self,route):
#         self.route=route
#         print(self.route)
# ref=Bus()
# ref.setvalue("perinthalmanna")
# ref.setval("ksrtc","white","KL23RTC456")
#
# 2.
# class Person:
#     def set(self,name,age):
#         self.name=name
#         self.age=age
#         print(self.name,self.age)
# class Child:
#     def setval(self,std,school):
#         self.std=std
#         self.school=school
#         print(self.std,self.school)
# class Student(Person,Child):
#     def setvalue(self,mark,dept):
#         self.mark=mark
#         self.dept=dept
#         print(self.mark,self.dept)
# ref=Student()
# ref.setvalue(85,"C.S")
# ref.setval("first","P T M H S S")
# ref.set("anu",23)
#
# 3.
# class Book:
#     def setvalue(self,Library_name,book_name,author,pages):
#         self.Library_name=Library_name
#         self.book_name=book_name
#         self.author=author
#         self.pages=pages
#         print(self.Library_name)
#         print(self.book_name)
#         print(self.author)
#         print(self.pages)
# ref=Book()
# ref.setvalue("oxford","one hundred years of solitude","gabriel",450)
#
# 4.
# class Animal:
#     def __init__(self,type,breed):
#         self.type=type
#         self.breed=breed
#     def printvalue(self):
#         print(self.type,self.breed)
# class Dog(Animal):
#     def __init__(self,color,name,type,breed):
#         super().__init__(type,breed)
#         self.color=color
#         self.name=name
#     def printv(self):
#         print(self.color,self.name)
#
# ref=Dog("black","tomy","domestic","pug")
# ref.printv()
# ref.printvalue()
#
# 13
# even=lambda n:n%2==0
# print(even(3))
#
# 12.
# it is called two string method.if we print our reference ,we get a memmory address
# each and every object has their unique properties or attributes.so we can commonize our reference
# using one of the attribute.
#
# two string method only contain strings ,if we want to add a integer,firsly convert into a string using "str".
# and if we want to add more values into it ,use "+" symbol,do not use commas
# class Vehicle:
#     def __init__(self,model,regno,clr):
#         self.model=model
#         self.regno=regno
#         self.clr=clr
#     def print(self):
#         print(self.model)
#         print(self.regno)
#         print(self.clr)
#     def __str__(self):
#         return self.model+" "+str(self.regno)
# veh = Vehicle("BMW", 1516, "BLUE")
# veh.print()
# print(veh)
# 11.
# "[^a][0-9]*[b$]"
# import re
# n=input("enter :")
# x="(^a[0-9]+b$)"
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")
# 10.
# import re
# n=input("enter :")
# x="([A-Z]{1}[a-z]+)"  #"(^[A-Z][a-z]+)"
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")
#
# 9.
# import re
# n=input("enter :")
# x="(^[A-Z]{1}\w{5,10}[A-Z]{1}$)"  #{3,8}
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")
# #

#
# 8
# a=[1,2,3,4,5]
# index=int(input("enter index="))
# try:
#     print(a[index])
# except:
#     print("index not in list")
# finally:
#     print("in finally")
#
#6.
# class Student:
#     def __init__(self,name,rollno,course,mark):
#         self.name=name
#         self.rollno=rollno
#         self.course=course
#         self.mark=mark
#
#     def printdata(self):
#         print(self.name)
#         print(self.rollno)
#         print(self.course)
#         print(self.mark)
#
# lst=[]
# f=open("wrk","r")
# for i in f:
#     d=i.rstrip("\n").split(",")
#     print(d)
#     name=d[0]
#     rollno=d[1]
#     course=d[2]
#     mark=d[3]
#     s1=Student(name,rollno,course,mark)
#     s1.printdata()
#     lst.append(s1)
#
# # print(lst)
# mark=[]
# for st in lst:
#     mark.append(st.mark)
# print(mark)
# for st in lst:
#     if (st.mark==max(mark)):
#         print(st.rollno,st.name,st.course,st.mark)

#7.phone number validation
