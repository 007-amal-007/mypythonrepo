a=int(input("enter a number:"))
flag=0
if a>1:
    for i in range(2,a):
        if a % i ==0:
            break
    else:
        flag=1
if flag==1:
    print("prime")
else:
    print("not prime")













