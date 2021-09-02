import re
x='[A-Z]'
matcher=re.finditer(x,"abt c@5kAz")
for match in matcher:
    print("index position:",match.start()," ",match.group())