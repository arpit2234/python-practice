a=20
num_guass =1
print("You can gauss up to 9 times maximum")

while(num_guass<=9):
    guass_num=int(input("Input your guass"))
    if(guass_num<a):
          print("your gauss is low")
    elif(guass_num>a):
        print("your gauss is High")
    else:
        print("your guass is right")
        break
    
    print(9-num_guass,"guass are left")
    num_guass=num_guass+1


if(num_guass>9):
    print("you exceeded number of guasses")
    
    
   

    
 
    




   





