# map operators to function
class A():
    def __init__(self,name,number):
        self.name=name
        self.number=number
    def __add__(self, other):
        return self.number+ other.number
    def __eq__(self, other):
        return self.name==other.name
    def __repr__(self):
        return "i am in repr"

    def __str__(self):
        return "i am in str"


one=A("Manan",10)
two=A("Manan",20)
# three=A("Dipak",30)
print(one)