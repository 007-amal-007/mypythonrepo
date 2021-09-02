def add(a,b):
    print(a+b)
def subtract(a,b):
    print(a-b)
def multiply(a,b):
    print(a*b)
def division(a,b):
    print(a/b)

print("select operation")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.division")

while True:
    choice=int(input("enter the choice"))
    num1 =float(input("enter a number"))
    num2=float(input("enter a number"))
    if choice ==1:
        (add(num1,num2))
    elif choice ==2:
        (subtract(num1,num2))
    elif choice==3:
        (multiply(num1,num2))
    elif choice==4:
        (division(num1,num2))
    else:
        print("invalid choice")