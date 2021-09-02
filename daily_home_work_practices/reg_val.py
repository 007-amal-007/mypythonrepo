import re
x='([L][U][M]\d{2}[P][Y]\d{3}$)'
f1=open("reg","r")
f2=open("reg_w","w")
for i in f1:
    # print(i)
    number=i.rstrip("\n")
    match=re.fullmatch(x,number)
    if match != None:
        f2.write(number)
        f2.write("\n")