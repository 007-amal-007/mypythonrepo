#while_loop........
#syntax


    # while(condition):
    #     body of loop
    #     incr/decr


#......................


a=0
while a<=10:
    print("hello")
    a=a+1
    #a+=1



i=10
while i>0:
    print(i)
    i-=1



num=int(input("enter a number to get multiplication table :"))
i=1
while i <= 10:
    mul=num*i
    print(i,"*",num,"=",mul)
    i=i+1