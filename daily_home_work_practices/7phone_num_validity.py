import re
f1=open("phone_num","r")
f2=open("phone_num_write","w")
x='[+][9][1]\d{10}$'
for num in f1:
    number=num.strip("\n")
    matcher=re.fullmatch(x,number)
    if matcher !=None:
        f2.write(num)
