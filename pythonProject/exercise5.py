def getdate():
    """Gives you current date and time"""
    import datetime
    return datetime.datetime.now()
#MAIN FUNCTION
def HMS():
    """ This function is used for Health Management System for 3 People  """
    #LIST OF USERS
    user=["MANAN","HARSH","YASH"]
    #Diet data
    dd={1:"manandiet.txt",2:"pokardiet.txt",3:"yashdiet.txt"}
    #Exercise data
    ed={1:"mananexc.txt",2:"pokarexc.txt",3:"yashexc.txt"}
    while(1):
        try:
            print("WHAT DO YOU WANT TO DO?")
            print("PRESS 1 FOR LOGIN:")
            print("PRESS 2 FOR RETRIEVE:")
            #choice number 1
            ch1=int(input())
            if(ch1==0 or ch1>2):
                print("Enter 1 and 2 only")
                continue
            else:
                print("There you go.......")
                break
        except:
            print("Please Enter 1 or 2 only :-")

#Code for login data
    if(ch1 == 1):
        while(1):
            try:
                print("\"\"You are logged in\"\"")
                print("Press 1 to Check Diet")
                print("Press 2 to check Exercise")
                #choice number 2
                ch2 = int(input())
                if(ch2>2 or ch2<=0):
                    print("Please Enter 1 or 2 only :-")
                    continue
                else:
                    break
            except:
                print("Please Enter 1 or 2 only :-")


        if(ch2 == 1):
            count = 1
            print("Whose diet you want to check")
            for i in user:
                print("PRESS", count, "for the user :-",i)
                count=count+1

    #user input
            while (1):
                try:
                    ui=int(input())
                    if (ui > len(user) or ui<=0):
                        print("Input is incorrect")
                        continue
                    else:
                        break
                except:
                    print("Enter correct value")

            with open(dd[ui]) as f:
                print("[",getdate(),"]",end="")
                print(f.read())
                print("thank you")
            while (1):
                try:
                    print("Do you want to print again?")
                    print("Press 1=Yes", "2=No")
                    x = int(input())
                    if (int(x) == 0 or int(x) > 2):
                        print("Enter 1 and 2 only")
                        continue
                    elif(int(x)==1):
                        with open(dd[ui]) as f:
                            print("[", getdate(), "]", end="")
                            print(f.read())
                    else:
                        break
                except:
                        print("Please Enter 1 or 2 only :-")

        if(ch2 == 2):
            count = 1
            print("Whose exercise you want to check")
            for i in user:
                print("PRESS", count, "for the user :-", i)
                count = count + 1
# user input
            while (1):
                    try:
                        ui = int(input())
                        if (ui > len(user) or ui <= 0):
                            print("Input is incorrect")
                            continue
                        else:
                            break
                    except:
                        print("Enter correct value")

            with open(ed[ui]) as f:
                    print("[", getdate(), "]", end="")
                    print(f.read())
                    print("thank you")
            while (1):
                try:
                    print("Do you want to print again?")
                    print("Press 1=Yes", "2=No")
                    x = int(input())
                    if (int(x) == 0 or int(x) > 2):
                        print("Enter 1 and 2 only")
                        continue
                    elif(int(x)==1):
                        with open(ed[ui]) as f:
                            print("[", getdate(), "]", end="")
                            print(f.read())
                    else:
                        break
                except:
                        print("Please Enter 1 or 2 only :-")
#Code to retrieve the data
    if(ch1 == 2):
        while (1):
            try:
                print("\"\"You are logged in\"\"")
                print("Press 1 to change Diet")
                print("Press 2 to change Exercise")
                # choice number 2
                ch2 = int(input())
                if (ch2 > 2 or ch2 <= 0):
                    print("Please Enter 1 or 2 only :-")
                    continue
                else:
                    break
            except:
                print("Please Enter 1 or 2 only :-")

        if (ch2 == 1):
            count = 1
            print("Whose diet you want to change")
            for i in user:
                print("PRESS", count, "for the user :-", i)
                count = count + 1

            # user input
            while (1):
                try:
                    ui = int(input())
                    if (ui > len(user) or ui <= 0):
                        print("Input is incorrect")
                        continue
                    else:
                        break
                except:
                    print("Enter correct value")

            with open(dd[ui],'w') as f:
                f.write(input())
            with open(dd[ui],'r') as f:
                print("new diet is")
                print("[", getdate(), "]", end="")
                print(f.read())

            while (1):
                try:
                    print("Do you want to edit again?")
                    print("Press 1=Yes", "2=No")
                    x = int(input())
                    if (int(x) == 0 or int(x) > 2):
                        print("Enter 1 and 2 only")
                        continue
                    elif(int(x)==1):
                        with open(dd[ui], 'w') as f:
                            f.write(input())
                        with open(dd[ui], 'r') as f:
                            print("new diet is")
                            print("[", getdate(), "]", end="")
                            print(f.read())
                    else:
                        break
                except:
                        print("Please Enter 1 or 2 only :-")

        if (ch2 == 2):
            count = 1
            print("Whose exercise you want to change")
            for i in user:
                print("PRESS", count, "for the user :-", i)
                count = count + 1
                # user input
            while (1):
                    try:
                        ui = int(input())
                        if (ui > len(user) or ui <= 0):
                            print("Input is incorrect")
                            continue
                        else:
                            break
                    except:
                        print("Enter correct value")

            with open(ed[ui],'w') as f:
                    f.write(input())
            with open(ed[ui],'r') as f:
                    print("new exercise is")
                    print("[", getdate(), "]", end="")
                    print(f.read())

            while (1):
                try:
                    print("Do you want to edit again?")
                    print("Press 1=Yes", "2=No")
                    x = int(input())
                    if (int(x) == 0 or int(x) > 2):
                        print("Enter 1 and 2 only")
                        continue
                    elif(int(x)==1):
                        with open(ed[ui], 'w') as f:
                            f.write(input())
                        with open(ed[ui], 'r') as f:
                            print("new exercise is")
                            print("[", getdate(), "]", end="")
                            print(f.read())
                    else:
                        break
                except:
                        print("Please Enter 1 or 2 only :-")
#for running again after one cycle
    while (1):
        try:
            print("Do you want to Run this Program again?")
            print("Press 1=Yes", "2=No")
            x = int(input())
            if (x == 0 or x > 2):
                print("Enter 1 and 2 only")
                continue
            else:
                break
        except:
            print("Please Enter 1 or 2 only :-")
    if (x == 1):
        HMS()
    else:
        print("Good Bye")

HMS()

