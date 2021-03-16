def gen(n):
    for i in range(n):
        yield i


# g= gen(5)
#
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
#
# s="Manan"
# itr=iter(s)
# print(itr.__next__())
# print(itr.__next__())
# print(itr.__next__())
# print(itr.__next__())
# print(itr.__next__())

def fibo(n):

   while True:
        if n==0:
            yield 0
        elif n==1:
            yield 1
        else:
            x= fibo(n-2) + fibo(n-1)
            yield x




g=gen(5)
f=fibo(10)
print(f.__next__())
print(f.__next__())




