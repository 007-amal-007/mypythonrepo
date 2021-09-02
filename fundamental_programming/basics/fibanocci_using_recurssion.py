def rec_fib(n):
    if n <= 1:      #0<=1 T , 1<=1 T , 2<=0 F ,
        return n    #0 , 1 ,
    else:                              #
        return rec_fib(n-1) + rec_fib(n-2)

nterms=10

print("fibanocci sequence :")
for i in range(nterms):
    print(rec_fib(i))

    #    0,1,2,3,4,5,6,7,8,9
    #    1st = 0
    #    2nd = 1
    #    3rd = 2