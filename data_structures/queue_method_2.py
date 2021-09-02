que=[]
size=int(input("enter size:"))
front=0
rear=0
n=0
def insert():
    global que,size,front,rear
    if rear >=size:
        print("queue is full!!")
    else:
        e=int(input("enter an element to insert:"))
        que.insert(rear,e)
        rear=rear+1

        for i in range(front,rear):
            print(que[i])
def delete():
    global size,que,front,rear
    if front==rear:
        print("queue is empty!!.")
    else:
        front=front+1

        for i in range(front,rear):
            print(que[i])

while n!=1:
    print("select an operation to perform:")
    opt=int(input("1.enque \n2.dequeue \n"))
    if opt == 1:
        insert()
    elif opt==2:
        delete()
    else:
        print("invalid")
    n=int(input("press 0 to continue.press 1 to exit"))
