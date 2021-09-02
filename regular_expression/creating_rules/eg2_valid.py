import re
x='[0-9]{2}[k][g]'
# n="56kg"
n=input("enter kg:")
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")