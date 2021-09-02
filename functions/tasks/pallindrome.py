#pallindrome or not

a=input("enter a string :")
b=a[::-1]
print(b)
if a==b:
    print("pallindrome")
else:
    print("not pallindrome")