def dec1(func):
    def executor():
        print("Thank you for entering value")
        func()
        print("please come again")
    return executor
@dec1
def sum1():
    print("enter two numbers")
    n1 = int(input("enter first number"))
    n2 = int(input("enter second number"))
    print(n1+n2)


sum1()