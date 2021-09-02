num=int(input("enter a number to print multiplication table up to 10 ="))
for tab_len in range(1,11):
    mul=num*tab_len
    print(tab_len,"*",num,"=",mul)