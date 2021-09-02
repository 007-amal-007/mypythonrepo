print("VACCINATION WEBSITE..")
name=input("enter your name:")
age=int(input("enter your age:"))
if age<18:
    raise Exception("you are not eligible for vaccination !!!")
else:
    print("you are eligible")
