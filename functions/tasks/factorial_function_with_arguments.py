def fac(num):
    mul=1
    if num>0:
        for i in range(1,num+1):
            mul=mul*i
        print(mul)
    elif num==0:
        print("factorial of 0 is 1")
    else:
        print("negative numbers doesn't have factorials")
fac(5)










