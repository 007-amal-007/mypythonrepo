#1.KEEPS ORDER  == stored in continous locations
#2.SUPPORT DUPLICATION
#3.HETEROGENIOUS
#4.NESTING IS POSSIBLE
#5.MUTABLE

# list=[1,2,3,4,5,12,0,1,2]
# print(list)
# print(type(list))
# for i in list:
#     print(i)
# l=[1,2,3,4,"hello",0,2,34,1,True]
# print(l)


#to create empty list
list=[]
list.append(8)
list.append("hello")
print(type(list))
print(list)

#nesting in list
list1=[1,2,[2,4,5,6,[1,2,3]]]
list1.remove(2)
# list1.clear()
# del list1
print(list1)

a=[1,4,5,62,9,7,2,6,3]
a.sort()

# INDEXING
list=[1,2,3,4,5,6,7,8,9]
print(list[-1])     #print last element
print(list[3])
print(list[0])