def fun1(fun2):
    print("bfore excute")
    fun2()
    print("after excute")


@fun1
def fun3():
    print("arpit is here123")


