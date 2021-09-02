import re

x="^a"
r="aaa abc aaaa cga"
# r="vac aa bca"
matcher=re.finditer(x,r)
for match in matcher:
    print("starting index position:",match.start()," ",match.group())