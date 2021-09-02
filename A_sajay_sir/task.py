lst=[2,4,6] #[10,8,6] [4+6,2+6,2+4]  [12-2,12-4,12-6]
# lst=[3,5,7] #[12,10,8] [5+7,3+7,3+5]

#1.
total=sum(lst)
op=[]
for num in lst:
    op.append(total-num)    #op=[total-num for num in lst
print(op)

#2.
print(list(map(lambda num:total-num,lst)))

#3.

#? sum of pairs
lst=[1,2,3,4,5]    #6=4+2
#1.
# total=6          #7=3+4  7=5+2
# for i in range(0,len(lst)):
#     for j in range(i+1,len(lst)):
#         if(lst[i]+lst[j]==6):
#             print(lst[i],lst[j])

#2.
low=0
upp=len(lst)-1
pair=6
pairs=[]
while(low<upp):
    sum=lst[low]+lst[upp]
    if(sum==pair):
        pairs.append((lst[low],lst[upp]))
        low+=1
    elif(sum>pair):
        upp-=1
    elif(sum<pair):
        low+=1
print(pairs)

#3.





#find common elements from both list
lst=[]










