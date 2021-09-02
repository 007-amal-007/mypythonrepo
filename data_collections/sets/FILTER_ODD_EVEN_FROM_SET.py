s={1,2,3,4,5,6,7,8,9,12,33,44,55,78,39,44}
o=set()
e=set()
for i in s:
    if i % 2 == 0:
        e.add(i)

    else:
        o.add(i)
print("odd=",o,"\n","even=",e)
