print("how many rows you want=")
row=int(input())
print("Type 0 or 1")
a=int(input())
b=bool(a)

if b==True:
    for i in range(1,row+1):
        for j in range(1,i+1):
            print("*",end ="     ")
        print()
elif b==False:
    for i in range(row,0,-1):
        for j in range(1,i+1):
            print("*",emd ="    ")
        print()

