import random

def num_gauss(a,b,actual):
    num=int(input(f"Enter your guass between{a} and {b}  "))
    ngauss=1
    # while num !=actual:
    #     if num>actual:
    #         num=int(input("Enter a smaller numer\n"))
    #         ngauss+=1
    #     else:
    #         num=int(input("Enter a Higher numer\n"))
    #         ngauss+=1
    
    if num>actual:
        num=int(input("Enter a smaller numer\n"))
        ngauss+=1
    
    elif num<actual:
        num=int(input("Enter a Higher numer\n"))
        ngauss+=1
    else:
        print("your gauss is correct")

    return ngauss
    

if __name__=="__main__":
    a=int(input("Enter the number of a=\n"))
    b=int(input("Enter the number of b=\n"))
    actual1= random. randint(a,b)

    print("player 1 turn\n")
    g1=num_gauss(a,b,actual1)
    print(f"Player 1 took {g1} guesses")
    print("player 2 turn\n")
    actual2= random. randint(a,b)
    g2=num_gauss(a,b,actual2)
    print(f"Player 2 took {g2} guesses")

    if g1>g2:
        print("player 2 won")
    elif g1<g2:
        print("player 1 won")
    else:
        print("it's a tie")