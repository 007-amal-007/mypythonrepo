# s1={1,2,3,4,5,6,7}
# s2={5,6,7,8,9,10,11}
# s3=set()
# for i in s1:
#     if i in s2:
#         s3.add(i)
# print(s3)

#can not use arithemetic operators directil ,we can use
#union,intersection,difference oprrators with set
# print(s1 + s2)

a={1,2,3,4,5,6,7}
b={3,4,5,6,7,8,9,0}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(b.difference(a))






