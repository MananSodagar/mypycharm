# i=0
# max=int(input("Enter number"))
# while(1):
#     if(i%2==0):
#         i = i + 1
#         continue
#
#     if(i<max):
#         print("=", i,end=(" "))
#         i=i+1
#     else:
#         break
# print("you are out")

# i=int(input("Enter number"))
while(1):
    i = int(input("Enter number"))
    if(i<100):

        print("Enter another number")
        continue

    if(i>=100):
        print("congratulations you enterd correct number")
        break
print("you are out")
