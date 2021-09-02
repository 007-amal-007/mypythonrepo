import re

x="a{2}"
r="aaa abc aaaa cga"
matcher=re.finditer(x,r)
for match in matcher:
    print("starting index position:",match.start()," ",match.group())