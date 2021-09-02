# a={1,2,3,4,5}
# print(a)
# print(type(a))
#
# b={5,6,7,8,9}
# print(b)
#
#
# #to create empty set
# a=set()
# #to add elements
# a.add(2)
# a.add(4)
# a.add(6)
# a.add(8)
# # 1.set is a "HETEROGENIOUS":we can add different types of elements like string,float,bool
# a.add(2.5)
# a.add("sifla")
# a.add(True)
# print(a)
# print(type(a))
#
#
#
# # 2.set do "NOT KEEP THE ORDER" that we given ,
# #it arrange elements either in ascending or descending order .
# c={2,8,5,0,1,3,7,9}
# print(c)


# # 3.set does not support "DUPLICATION" of elements
# a={1,2,3,1,2}
# #it do not print " True " bcz True ==1
# a.add(True)
# print(a)


#we iterate elements of a set by using for loop
# b={"hello",5,6,4,7,8,8.6,False}
# print(b)
# for i in b:
#     print(i)


#sets are "MUTABLE"
# s={1,2,3,4,5,6,7,8,9,21}
# s.remove(2)       #to a single element
# s.clear()         #to clear all elements
# del s             #to delete the whole set
# print(s)


#  "NESTING NOT POSSIBLE"
a={1,2,{3,4}}
print(a)


#1.NOT KEEPING ORDER
#2.NOT SUPPORT DUPLICATION ELEMENTS
#3.HETEROGENEOUS
#4.MUTABLE
#5.NESTING NOT POSSIBLE

