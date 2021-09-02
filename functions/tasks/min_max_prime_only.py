min=int(input("enter min range :"))
max=int(input("enter max range :"))
for a in range(min,max+1):   #a=prime
    if a>1:
        for i in range(2,a):
            if a%i==0:
                break
        else:
            print(a)














