class Student:
    leaves=18
    def __init__(self,name,std,village):
        self.name=name
        self.std=std
        self.village=village

    @classmethod
    def change_leave(cls,newleave):
        cls.leaves=newleave
    

    @classmethod
    def str(cls,string):
        # params=string.split("-")
        # print(params)
        # return cls(params[0],params[1],params[2])
        return cls (*string.split("-"))


arpit=Student("arpit",12,"kampri")
arpit2=Student("arpit2",15,"chikhla")
arpit3=Student.str("arpit3-21-rola")



print(arpit3.std)



    
       


    