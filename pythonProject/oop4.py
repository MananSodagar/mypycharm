class DADA():
    @property
    def __init__(self,r):
        self.noh1=r

    def create(self,s):
        self.noh1=s
        return 0

    @create.setter
    def create(self,s):
        self.noh1=s
        return 0

class PAPA(DADA):
    noh2=10
class Me(PAPA):
   noh3=8



m=Me()
p=PAPA()
d=DADA(10)



x=d.create(20)
print(x)