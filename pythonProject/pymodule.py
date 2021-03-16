# import math
# import pandas as pd
# import numpy as ny
#
# num=pd.Series(ny.random.rand(10))
#
# # a=math.fsum([120,1,54,645])
# print(num)
import random
# x=random.getstate()
# random.setstate()
# print(x)

# statebefore=random.getstate()
# #print a random number:
# print(random.random())
#
# #capture the state:
# state = random.getstate()
#
# #print another random number:
# print(random.random())
#
# #restore the state:
# random.setstate(state)
#
# #and the next random number should be the same as when you captured the state:
# print(random.random())
#
# random.setstate(statebefore)
# print(random.random())

for i in range(random.randint(1,100)):
    print(i+1)