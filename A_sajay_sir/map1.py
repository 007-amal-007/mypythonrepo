#?print squares of all number
#?print even numbers from list
#?lowest number from list

# #MAP
#syntax:
    #map(function,list/iterables)

lst=[2,3,4,5,6]
#?print squares of all numbe
#normal fucn
def square(n):
    return(n**2)

sqaures=list(map(square,lst))
print(square)        #we get an object reference .back it as a list .use "list()"



# # cube
# # cubes=lambda n:n**3
# # print(cubes(3))
#
# cubes=list(map(lambda n:n**3,lst))
# print(cubes)
#
#

#FILTER
# lst=[2,3,4,5,6]
# def even(num):
#     return  num%2==0

# evens=list(filter(even(),lst))
# print(evens)
# lst=[2,3,4,5,6]
# evens=list(filter(lambda num:num%2==0,lst))
# print(evens)
#
# odds=list(filter(lambda num:num%2!=0,lst))
# print(odds)


#REDUCE
# from functools import reduce
# max=reduce(lambda num1,num2:num2 if num1<num2 else num1)
# print(max)

