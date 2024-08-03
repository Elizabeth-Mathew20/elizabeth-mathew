# row=5
# for i in range(10):
#     for j in range (i+1):
#         print("*",end="  ")
#     print()    





row=int(input("enter a numnber"))
k=0
for i in range(1,row+1):
    for j in range(1,(row-i)+1):
        print(end="  ")
    while k!=(2*i-1):
        print("*",end="       ")
        k+=1
    k=0
    print()        




# row=int(input("enter the number"))
# k=0
# r=0
# c=0
# for i in range(1,row+1):
#     for j in range(1,(row-i)+1):
#            print(end=" ")
#            r+=1
#     while k!=(2*i-1):
#         if r<=row-1:
#              print(i+k,end=" ") 
#              r+=1
#         else:
#             c+=1
#             print(i+k-(2*c),end=" ")
#         k+=1
#     r=c=k=0
#     print()


    



        


