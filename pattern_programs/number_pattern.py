# #1
# # 2 3
# # 4 5 6
#
# # def num_pattern():
# num=1
# for i in range(0,5):
#     for j in range(0,i):
#         print(num,end=" ")
#         num+=1
#     print("\r")
#
#



# 1
#1 2
#1 2 3
#1 2 3 4


def pattern(n):                  #n=5

    for i in range(0,n):         # i= 0 1 2 3 4 (row)
        num = 1
        for j in range(0,i):
            print(num,end=" ")
            num=num+1
        print("\r")
pattern(5)
