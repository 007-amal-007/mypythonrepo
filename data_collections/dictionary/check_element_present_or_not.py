dict={1:10,2:20,3:30,4:40,5:50,6:60}

def present_or_not(n):
    if n in dict:
        print(n,"present")
    else:
        print(n,"not present")

x=int(input("enter key="))
present_or_not()