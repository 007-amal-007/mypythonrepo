#print details of employee having salary above 15000rs

list=[(1,"anu",28,20000),(2,"vinu",23,15000),(3,"ram",25,10000)]
for i in list:
    # print(i)
    if i[-1] >= 15000:
        print(i)
