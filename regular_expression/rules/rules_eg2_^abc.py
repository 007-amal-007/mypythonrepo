import re
x='[^abc]'
matcher=re.finditer(x,"abt c@5kzabc")
for match in matcher:
    print("index position:",match.start()," ",match.group())