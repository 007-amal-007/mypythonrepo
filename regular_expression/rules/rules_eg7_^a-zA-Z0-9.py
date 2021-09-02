import re
x='[^0-9a-zA-Z]'
matcher=re.finditer(x,"abt9 c@5kAz")
for match in matcher:
    print("index position:",match.start()," ",match.group())