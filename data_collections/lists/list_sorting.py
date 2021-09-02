my_list=[111,-15,-26,15,1,0,8,876,100,54,23,-64,23,76]
new_list=[]

while my_list:
    min=my_list[0]
    for i in my_list:
        if i< min:
            min = i
    new_list.append(min)
    my_list.remove(min)

print(new_list)
print(my_list)


#                       OR



lis=[-2,3,4,-5,16,7,10]
# length=

