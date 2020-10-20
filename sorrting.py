list=[2,5,1,8]
# size=int(input("enter size of list"))

# for i in range(size):
#     a=int(input("enter values you want in list"))
#     list.append(a)

print(list)

# def sort(list):
#     list.sort() 
#     return list
# a=sort(list)
# print(a)
  
reverse1=list[:]
reverse1.reverse()
reverse2=list[::-1]
print(f"Sorting by first method{reverse1}")
print(f"Sorting by second method{reverse2}")

reverse3=list[:]
for i in range(len(reverse3)//2):
    reverse3[i],reverse3[len(reverse3)-i-1]=reverse3[len(reverse3)-i-1],reverse3[i]
    # print(f"{i}reverse list is{reverse3} ")


print(f"Sorting by third method{reverse3}")

if reverse1==reverse2 and reverse1==reverse3:
    print("all list are same")