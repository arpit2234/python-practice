class Library:
    def __init__(self,list,name):
        self.booklist=list
        self.name=name
        self.lendDict={}

    def displaybooks(self):
        print(f"we have follownin books in our library:{self.name}")
        for book in self.booklist:
            print(book)

    def lendbook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book data has been updated,you can take the book now")

        else:
            print(f"the book is already being used by{self.lendDict[book]}")

    def addbook(self,book):
        self.booklist.append(book)
        print("book has been added tp the book list")
    def returnbook(self,book):
        self.lendDict.pop(book)
        



if __name__=='__main__':
    harry=Library(['python','rich dad poor dad','harry porter','c++ basics','Algoritham by CLRS'],"Codewithhaary")

    while(True):
        print(f"welcome to {harry.name} library,Enter your choice to continue")
        print("1.Display books")
        print("2.Lend a books")
        print("3.Add a books")
        print("4.Return a books")
        user_choice=input()

        if user_choice not in ['1','2','3','4']:
            print("enter valid value")
            continue
        else:
            user_choice=int(user_choice)


        

        if user_choice==1:
            harry.displaybooks()

        elif user_choice==2:
            user=input("Enter your name:")
            book=input("Enter name of the book you want to lend:")
            harry.lendbook(user,book)
             
        
        elif user_choice==3:
            book=input("Enter name of the book you want to Add:")
            harry.addbook(book)
             
        
        elif user_choice==4:
            book=input("Enter name of the book you want to Return:")
            harry.returnbook(book)
            
        else:
            print("Not a valid option")



        
        print("Press q for exit and C for Continue")
        user_choice2=""
        while(user_choice2!="q" and user_choice2!="c"):
            user_choice2=input()
        if user_choice2=="q":
            exit()
        elif user_choice2=="c":
            continue

        

        



           

    