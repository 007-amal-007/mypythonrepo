#starting with a and ending with b
#ab augyighoerhg47yfge8rgb aaabbbb a564';';,lgb

import re

n=input("enter a string:")
x="[^a][a-zA-z0-9]+[\W][b$]"
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")