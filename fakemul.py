import random
def rohanmultiplication(number):
    wrong=random.randint(0,9)
    table=[i*number for i in range(1,11)]
    table[wrong]=table[wrong]+random.randint(0,number//2)
    return table

def iscorrect(table,number):
    for i in range(1,11):
        if table[i-1]!=i*number:
            return i-1



    return None

if __name__=="__main__":
    # print(rohanmultiplication(7))
    number=int(input("Enter your Number ="))
    mytable=rohanmultiplication(number)
    print(mytable)
    wrongindex=iscorrect(mytable,number)
    print(f"the table is wrong at index {wrongindex}")

    