print("Welcome to the Library")
bl=[]
ul={}



class Mylib():
    def __init__(self,name):
        self.name=name
        print(f" you are logged in as {self.name}")
    def Main(self):
     while True:

        print("Enetr 1.Display books")
        print("Enetr 2.Add book")
        print("Enetr 3.Lent book")
        print("Enetr 4.Return book")
        print("Enter 5 Exit")


        ui= int(input("Please enter your input:--"))

        if(ui==1):
            print(bl)
            print(f"the books on hold are {ul.items()}")
        elif(ui==2):
            print("Enter the name of BOOK")
            ab=input()
            bl.append(ab)

        elif(ui==3):
            print("Which book you want to lent")
            lb=input()

            for book in bl:
                if(lb==book):
                    bl.remove(lb)
                    ul.update({lb:self.name})
                    print(ul.items())


                    print("This book is successfully lended")
                    break
            else:
                print("Enter right value")

        elif(ui==4):

            print("Which book you want to remove")
            rb = input()

            for i in bl:
                if (i != rb):
                    bl.append(rb)
                    ul.pop(rb)
                    print(f"This book name{rb} is successfully return by {ul.get(rb)}")
                    break
            else:
                print("Enter right value")

        elif(ui==5):
            break
        else:
            print("Please enter right input")




while True:
    print("press 1 enter as manan")
    print("press 2 enter as jerry")
    print("press 3 enter as carry")
    print("press 4 to exit")

    n=int(input())

    if n==1:
        manan = Mylib("Manan")
        manan.Main()

    elif n==2:
        jerry = Mylib("jerry")
        jerry.Main()
    elif n==3:
        cerry = Mylib("carry")
        cerry.Main()
    elif n==4:
        break







