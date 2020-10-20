class Student:
    leaves=18
    def __init__(self,name,std,village):
        self.name=name
        self.std=std
        self.village=village

    @classmethod
    def change_leave(cls,newleave):
        cls.leaves=newleave
    

    
    




arpit=Student("arpit",12,"kampri")
arpit2=Student("arpit2",15,"chikhla")



arpit.change_leave(23)

print(arpit.leaves) 