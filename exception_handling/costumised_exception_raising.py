a=int(input("enter first:"))
b=int(input("enter second:"))
if b>a:
    raise Exception("second number is greater")
else:
    print(a/b)