num=int(input("enter number to get factorial:"))
fact=1
if num>0:
    for i in range(1,num+1):
        fact=fact*i
    print(fact)
elif num==0:
    print("factorial is 1")
else:
    print("enter a positive number,factorial doesnt exist for negative numbers")
