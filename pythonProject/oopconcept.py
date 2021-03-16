class Employee:
    name="employee"
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
    name2="rajeshh"
    def __init__(self):
        return 0





a=Employee("ram",1,1920,"bharuch")
b=Employee(1,2,3,4)
c=Prog()
print(Prog.name2)
# c=Employee.change_args("x=y=z=a")
# a.name="manan"
# b.name="raju"
a.sum("xxx")
print(Employee.name)
Employee.name="workor"
# print(Employee.name)
a.myprint()
print(a.summer(2,3))
b.myprint()
