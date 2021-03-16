class First():
    x=1
class Second():
    x=2
class Third(Second,First):
   pass


f=First()
s=Second()
t=Third()

print(t.x)