import re
f2=open("lum_reg","w")
rule="([L][U][M]\D{2}[P][Y]{3}$)"
f=open("valid_reg","r")
for num in f:
    number=num.rstrip("\n")
    matcher=re.fullmatch(rule,number)
    if matcher !=None:
        f2.write(number)
        f2.write("\n")