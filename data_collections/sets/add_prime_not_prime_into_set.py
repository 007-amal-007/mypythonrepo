s={1,2,3,4,5,6,7,88,77,99,33,11}
p=set()
np=set()
for i in s:                     #
    if i >= 1:
        for j in range(2,i):
            if i % j == 0:
                np.add(i)
                break
        else:
            p.add(i)
print(p)
print(np)
