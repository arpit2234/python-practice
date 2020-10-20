apple=int(input("Enter the number of Apple:\n"))
mn=int(input("Enter the Minimum number of range:\n"))
mx=int(input("Enter the Maximum number of range:\n"))


if mx==mn:
    print("this is not range")
    exit()

for i in range(mn,mx+1):
    if apple%i==0:
        print(f"{i} is a divisor of {apple}")
    
    else:
        print(f"{i} is not a divisor of {apple}")
    




