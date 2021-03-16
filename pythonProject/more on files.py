with open("filesiopractice.txt") as f:
    a=f.read()
    print(a)
    f.seek(10)
    print(f.read())
    print(f.tell())
    f.seek(0)
    print(f.readlines())

f=open("filesiopractice.txt")
print(f.read())
f.close()
