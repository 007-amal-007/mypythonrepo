# a="malayalam"
# for i in a:
#     print(a.count("m"))
#     break





a="malayalam"
e=input("enter an element to count :")
count=0
for i in a:
    if e in i:
        count=count+1
print(count)