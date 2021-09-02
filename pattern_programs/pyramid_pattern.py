  #    *
  #   * *
  #  * * *
  # * * * *



k=6
for i in range(0,6):                  #row
    for r in range(k):                #spacing
        print(end=" ")
    k=k-1
    for j in range(0,i+1):              #star
        print("*", end=" ")
    print("\r")








