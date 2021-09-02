import re
n=input("enter your vehicle regno:")
x="[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}" #'[K][L]\d{2}\d{4}$'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")