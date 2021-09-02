amount=5000
withdraw=int(input("enter amount to withdraw :"))
if withdraw>amount:
    print("insufficient balance")
else:
    print("your current balance is :",amount - withdraw)



# a=5000
# w=int(input("enter amount to withdraw :"))
# if w<=a:
#     b=a-w
#     print("balance",b)
# else:
#     print("insufficient")
