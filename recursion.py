def factorial(n):
    fac=1
    for i in range(n):
        fac=fac*(i+1)
    return fac

def fact(n):
    if n==1:
        return 1
    else :
        return n*fact(n-1)

def sumfibo(n):
    if n==1:
         return 0
    elif n==2:
        return 1
    else:
        return sumfibo(n-1)+sumfibo(n-2)
   

    
       

num=int(input("enter your number"))
print(factorial(num))
print(fact(num))
print(sumfibo(num))