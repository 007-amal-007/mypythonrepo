a=[4,5,7,8,9,0,3,1,2,33,45,67,87,65,3,11,23,93,72,51,77,88,99,16]
def bsearch():
    a.sort()
    print(a)
    element=int(input("enter elementn you want to find ="))
    flag=0
    low=0
    upp=0
    upp=len(a)-1
    while low <= upp:
        mid = (low + upp) // 2
        if element > a[mid]:
            low = mid + 1
        elif element < a[mid]:
            upp = mid - 1
        elif element == a[mid]:
            flag=1
            break
    if flag ==1:
        print("found")
    else:
        print("not found")
bsearch()