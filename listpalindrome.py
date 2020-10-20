
def next_palindrome(n):
    n=n+1
    while not is_palindrome(n):
        n+=1
    return n

def is_palindrome(n):
    return str(n)==str(n)[::-1]


if __name__=="__main__":
    size=(int(input("Enter size of the list =")))
    numlist=[]

    for i in range(size):
        numlist.append(int(input("Enter the number of the list=\n")))

    print(f"You have entered {numlist}")

    # newlist=[]
    # for element in numlist:
    #     if element>10:
    #         n=next_palindrome(element)
    #         newlist.append(n)
    #     else:
    #         newlist.append(element)

    # print(f"your ooutput is {newlist}")

    # one linear
    print(f"Your out put : {[numlist[i] if numlist[i]<10 else next_palindrome(numlist[i]) for i in range(size)]}")