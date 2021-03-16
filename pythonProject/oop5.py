class A():
    var1="inside class a"
    def __init__(self):
        self.var1="inside a's function"
class B(A):

    def __init__(self):

        self.var1="inside bs function"
        super().__init__()

    var1="inside class b"


a=A()
b=B()

print(b.var1)