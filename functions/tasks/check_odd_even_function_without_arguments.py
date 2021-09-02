num=int(input("enter a number :"))
def odd_even():
    if num>0:
        if num % 2 == 0:
            print("even")
        else:
            print("odd")
    else:
        print("enter a +ve number")
odd_even()