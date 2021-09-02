import re

x="a{2,3}"
r="aaa abc aaaaa cga"
matcher=re.finditer(x,r)
for match in matcher:
    print("starting index position:",match.start()," ",match.group())