#FIFO
#insertion....enqueue
#deletion....dequeue

q=[]
size=int(input("enter size:"))
front=0
n=0
def insertion():
    global front,size
    if front>size:
        print("queue is full...")
    else:
        p=int(input("enter the element u want to insert:"))
        q.append(p)
        front=front+1
def deletion():
    global front
    if front<=0:
        print("que is empty...")
    else:
        del q[0]
        front=front-1
def display():
    print(q)
while(n!=1):
    print("enter the operation u want to perform:")
    opt=int(input("press 1)insertion 2)deletion 3)display"))
    if(opt==1):
        insertion()
    elif(opt==2):
        deletion()
    elif(opt==3):
        display()
    else:
        print("invalid")
    n=int(input("do u want to continue press 1 for exit"))

