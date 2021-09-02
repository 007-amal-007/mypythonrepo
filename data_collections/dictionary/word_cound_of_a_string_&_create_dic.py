count={}
data=input("enter=")
words=data.split(" ")  #list
print(words)
for word in words:
    print(word)
    if word not in count:
        count.update({word:1})
    else:
        val=int(count[word])
        val=val+1
        count.update({word:val})
print(count)
