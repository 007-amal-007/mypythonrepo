a=int(input("enter first num:"))
b=int(input("enter second num:"))
try:
    div = a / b
    print(div)
except Exception as e:
    print(e.args)
finally:
    print("in finally")