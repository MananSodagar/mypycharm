class Employee:
    name3="employee"
    def myprint(self):
        print( f"{self.name} {self.city} {self.birth} {self.rank}\n")

    def __init__(self,name,rank,birth,city):
        self.name=name
        self.rank=rank
        self.birth=birth
        self.city=city


    @classmethod

    def sum(cls,n):
        cls.name=n

    @classmethod
    def change_args(cls,str):

        return cls(*str.split("="))

    @staticmethod
    def summer(x,y):
        return x+y
class Prog(Employee):
    name2="fwefwfwef"
    def __init__(self,name,rank,birth,city):
        self.name=name
        self.rank=rank
        self.birth=birth
        self.city=city

w=Prog(1,2,3,4)
e=Employee(1,2,3,4)
print(e.name2)
