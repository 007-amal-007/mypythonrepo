# string=input("enter a string :")  #english
# vowels=' "a","e","i","o","u"'
# count=0
# for i in string:                  #e n g l i s h
#     if i in vowels:               # e i
#          count=count+1
#     else:
#         pass
# print("vowels count of",string,"is",count)



while True:
    a=input("string :")
    count=0
    for i in a:
        if i in "aeiou":
            count+=1
        else:
            pass
    print("vowels count of",a,"is",count)
