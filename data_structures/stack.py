#LIFO - LAST IN FIRST OUT
#OPERATIONS
#     ADD = PUSH
#     REMOVE = POP
#     DISPLAY =
#SPECIFY THE SIZE OF THE STACK

stk=[]
size=int(input("enter the size:"))
top=0
n=0
def push():
    global top,size
    if(top>size):
        print("stack is full..!!")
    else:
        p=int(input("enter the u want to push:"))
        stk.append(p)
        top=top+1
def pop():
    global top,size
    if(top<=0):
        print("stack is empty")
    else:
        stk.pop()
        top=top-1
def display():
    print(stk)
while(n!=1):
    print("enter the operation u want to perform:")
    opt=int(input("press 1)push 2)pop 3)display"))
    if(opt==1):
        push()
    elif(opt==2):
        pop()
    elif(opt==3):
        display()
    else:
        print("invalid")
    n=int(input("do u want to continue press 0, press 1 for exit"))

