#Secret  number
num=76
#total number of guess availabe
guess=9
print("you have 10 guesses\n")
while(True):
    gnum=int(input("Enter the gussed number\n"))
    guess = guess - 1
    if gnum > num:
        print("guess less\n")
    elif gnum < num:
        print("guess big \n")
    elif gnum==num:
        print("YOU WON and",guess," guesses left")
        break #goes out of the while loop
    if guess==0:
       print("Game OVER")
       break

    print("Total guess left= ", guess)
