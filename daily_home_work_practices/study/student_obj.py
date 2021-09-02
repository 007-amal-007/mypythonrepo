dict={}
f1=open("student","r")
for i in f1:
    # print(i)
    new=i.split(" ")
    # print(new)
    for word in new:
        # print(word)
        if word not in dict:
            dict.update({word:1})
        else:
            val=int(dict[word])
            val=val+1
            dict.update({word:val})
print(dict)
