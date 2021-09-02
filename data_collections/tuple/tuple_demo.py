#more secure datas are store by using tuple : provide more security

#immutable
#keeps order
tupl=9,3,4,56,
# print(tupl)
tuple=(1,2,3,4,8,10,11,56,5,6,7)
# print(tuple)

#allow duplication
tuple=(1,2,3,4,5,6,7,1,2,3)
# print(tuple)

#heterogenous
tuple=(1,2,3,4,5,6,7,"hello","hi")
# print(tuple)

#nesting possible
tuple=(1,2,3,4,5,6,7,("hello",(1,2,3)))
# print(tuple)

#iterate by using for loop
tuple=(1,2,3,4,5,6,7)
# for i in tuple:
#     print(i)

tup=1,4,5,6,7,8,9,11,22,3,34,4,55,6,66
print(tup)
print("max value",max(tup))
print("min value",min(tup))
print("len",len(tup))            #length
print(tup[0])                    #indexing
print(tup[-1])
print(tup[1:4])                   #slicing


my_tuple=('a','p','p','l','e',)
print(my_tuple.count('p'))
print(my_tuple.index('p'))       #takes the first
