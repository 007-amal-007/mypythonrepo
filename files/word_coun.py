count={}
f=open("word_count",'r')
for n in f:
    wr=n.split(" ")
    #print(wr)
    for word in wr:
        if word not in count:
            count.update({word:1})
        else:
            val=int(count[word])
            val+=1
            count.update({word:val})
print(count)

