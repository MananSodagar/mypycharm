import random
""" 
program related to set state of Random number
state= random.getstate()
r=random.random()
print(r)
r1=random.random()
print(r1)
random.setstate(state)
r2=random.random()
print(r2)
"""

"""
prints an integer as given bits
x=random.getrandbits(1)
print(x)
"""
"""
x=random.randrange(2,10,2)
print(x)
"""

"""
for i in range(10):
    print(random.randint(2,10))
    
    a=["toy","bag","book","lidl","edeka","rewe"]
print(random.choices(a, weights=[5,1,1,1,1,1], k=10))

a = ["toy", "bag", "book", "lidl", "edeka", "rewe"]
print(a)
random.shuffle(a)
print(a)
print(random.sample(a,k=2))

for i in range(10):
    print(random.triangular(1, 10, 2))
"""






















