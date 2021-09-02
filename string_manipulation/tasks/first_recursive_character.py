a=input("enter a string :")   #apple
b=""
for i in a:     # i = a p p l e
    if i not in b:
        b=b+i

    else:
        print("first recurssive character in",a,"is",i)
        break  #it is used to print the first repeating character only ,not others only the first letter
