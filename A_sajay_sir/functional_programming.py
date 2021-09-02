def cube(n):
    print(n**3)
cube(5)

#lambda
cube=lambda  n:n**3
print(cube(3))


#find cubes of above list
lst=[2,3,4,5,6]

#normal:
list=[]
for num in lst:
    res=num**3
    list.append(res)
print(list)
