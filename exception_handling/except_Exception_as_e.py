lst=[1,2,3,4,5]
pos=int(input("enter index="))
try:
    print(lst[pos])
except Exception as e:
    print(e.args)
finally:
    print("inside")