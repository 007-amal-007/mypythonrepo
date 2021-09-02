#call the function again inside the function

def factorial(x):
    if x==0:
        return 1
    # if x==1:
    #     return 1
    # elif x==0:
    #     return 1
    else:
        return x * factorial(x-1)

    #x=5


num=int(input("enter the number :"))
print("the factorial is ",factorial(num))
