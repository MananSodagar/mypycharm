def logic():


        try:
            print("How many line of STARS do you want to print?")
            line = int(input())

            if (line != int()):
                print("There You Go")
        except:
            print("Enter again")
            logic()

        starlist = ["*" * line]


        while (1):
            print("for Top-Down PRESS 0")
            print("for Bottom-Up PRESS 1")
            b = input()
            if (b == '0'):
                break
            elif(b == '1'):
                break
            else:
                print("You enterd wrong value")
                print("Enter 0 or 1 only")


        if (int(b) == True):
            while (1):
                if (line > 0):
                    count = line
                    for raw in starlist:
                        for column in raw:
                            print(column * line)
                            line = line - 1
                else:
                    print("Do you want to try again? Press Y for YES and N for NO")
                    while (1):
                        yes = input()
                        if (yes == 'Y'):
                            logic()
                        elif (yes == 'N'):
                            break
                        else:
                            print("You enterd wrong value")
                            print("Enter Y or N only")
                    break


        if (int(b) == False):
            while (1):
                if (line > 0):
                    count = 1
                    for raw in starlist:
                        for column in raw:
                            print(column * count)
                            count = count + 1
                            line = line - 1
                else:
                    print("Do you want to try again? Press Y for YES and N for NO")
                    while (1):
                        yes = input()
                        if (yes == 'Y'):
                            logic()
                        elif (yes == 'N'):
                            break
                        else:
                            print("You enterd wrong value")
                            print("Enter Y or N only")
                    print("thank you")
                    quit()



logic()










