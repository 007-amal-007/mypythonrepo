num1=8
num2=2
num3=2
if num1>num2 and num2==num3:   #it works when both conditions are true
    print("hello")

if num1>num2 & num2==num3:   #here we can use & operator too
    print("hello")

if num1>num2 or num1>num3:     #it works when any of the condition is true
    print("hi")

