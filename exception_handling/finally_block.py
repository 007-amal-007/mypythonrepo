#finally block run after try & except
a=[1,2,3,4,5]
index=int(input("enter index="))
try:
    print(a[index])
except:
    print("index not in list")
finally:
    print("in finally")
















