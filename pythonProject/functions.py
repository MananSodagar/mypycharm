def calc(num1,num2):
    """This function adds two numbers"""
    print("the total is",num1+num2)

while(1):
    try:
        print("Enter first number\n")
        x=int(input())
        break

        continue
    except Exception as e:
        print("Enter correct value")
        print(e)

print("Enter second number\n")
y=int(input())

print(calc.__doc__)
calc(x,y)