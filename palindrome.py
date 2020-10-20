
def next_palindrome(n):
    n=n+1
    while not is_palindrome(n):
        n+=1
    return n

def is_palindrome(n):
    return str(n)==str(n)[::-1]
    



if __name__=="__main__":
    n=int(input("Enter of no test case"))
    number=[]

    for i in range(n):
        a =int(input("Enter the number=\n"))
        number.append(a)


    # print(number)
    for i in range(n):
        print(f"palindrome number for{number[i]} is {next_palindrome(number[i])} ")