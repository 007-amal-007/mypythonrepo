list=[11,22,34,45,0,1,2,3,4,5,6,7,8,9]
for i in list:
    min=list[0]
    if i < min:
        min = i
        print("min :",i)
        break

for i in list:
    max = list[0]
    if i > max:
         max = i
         print("max :",i)
         break


#
list=[11,22,34,45,0,1,2,3,4,5,6,7,8,9]
list.sort()
print(list)
print("min",list[0])
print("max",list[-1])



