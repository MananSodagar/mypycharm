# flase values 45*3=555,56+9=77,56/6=4

print("Enter the numbers")
num1=int(input("num 1"))
num2=int(input("num 2"))

print("press + to additon")
print("press - to substraction")
print("press * to multiplication")
print("press / to division")

operator=input("enter the operator")

if operator=="+" and num1==56 and num2==9:
    print("77")
elif operator=="*" and num1==45 and num2==3:
    print("555")
elif operator=="/"and num1==56 and num2==6:
    print("4")
elif operator=="+":
    print("The answer is:",num1+num2)
elif operator=="-":
    print("The answer is:",num1-num2)
elif operator=="*":
    print("The answer is:",num1*num2)
elif operator=="/":
    print("The answer is:",num1/num2)
else:
    print("enter correct operator")




