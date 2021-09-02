list=[1,2,3,4,5,6,7,8,9,0,11,22,33,44,56,34,23,29,88,99]
def linear_search(list):
    element=int(input("enter element you want to check :"))
    flag=0
    for i in list:
        if i==element:
            flag=1
            break
    if flag==0:
        print("not present")
    else:
        print("present")

linear_search(list)