a={1,2,3,4,5,6,7,8,9,10}
b=set()
for i in a:
    square=i**2       #
    b.add(square)     #b.add(i*i) or b.add(i**2)
print(b)