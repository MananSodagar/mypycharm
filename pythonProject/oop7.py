from abc import ABC,abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def area(self):
        return 0

class Circle(Shape):

    def __init__(self,r):
        self.r=r


    # def area(self):
    #    print(pi*self.r*self.r)


c=Circle(6)
c.area()