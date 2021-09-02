import re
n=input("enter phone no:")
x="[0-9]{10}"
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")