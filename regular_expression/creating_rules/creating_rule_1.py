#combination of upper case and lower case letters and it must ending with a number
#Abc6  fgRtggg7 gfghh8 DFGGH6
import re
n=input("enter :") #n="ABYGISDugvdkfcv6"
x="[a-zA-Z]*[0-9]{1}$"   #[a-zA-Z]+\d$  +minimum one number
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")
