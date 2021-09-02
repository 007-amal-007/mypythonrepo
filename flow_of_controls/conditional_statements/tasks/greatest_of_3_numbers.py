no1=int(input("enter no1: "))
no2=int(input("enter no2 :"))
no3=int(input("enter no3 :"))

# if no1>no2:
#     print("no1 is greater")
# elif no2>no3:
#     print("no2 is greater")
# elif no3>no1:
#     print("no3 is greater")
# else:
#     print("no1 ,no2 and no3 are equal")



if no1>no2 and no1>no3:
    print("no1 is greater")
elif no2>no1 and no2>no3:
    print("no2 is greater")
elif no3>no1 and no3>no2:
    print("no3 is greater")
else:
    print("all r equal")