import re
x='[a-zA-Z]'
matcher=re.finditer(x,"abt c@5kzabc")
for match in matcher:
    print("index position:",match.start()," ","group:",match.group())




