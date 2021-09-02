import re
n=input("enter indian phone no:")
x="[+][9][1][0-9]{10}"  #x="[+][9][1][0-9]{10}$"
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")