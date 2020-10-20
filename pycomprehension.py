# ls=[]



# for i in range(100):
#     if i%3==0:
#         ls.append(i)
    
# print(ls)
user_input = eval(input('Enter how many items you want: '))
user_choice = eval(input('Press\n'
                         '1 for List Comprehension\n'
                         '2 for Dictionary Comprehension\n'
                         '3 for Set Comprehension\n'))

if user_choice == 1:
    list1 = ['I am a good programmer' for i in range(user_input)]
    print(list1)

if user_choice == 2:
    dict1 = {i: 'I am a awesome programmer' for i in range(user_input)}
    print(dict1)

if user_choice == 3:
    set1 = {"you are the best programmer" for i in range(user_input)}
    print(set1)