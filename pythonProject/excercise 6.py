#Sanke Water Gun game
#snake wins vs water
# water against gun
# gun against snake

import random

print("You play this GAME against computer 10 times")
x=10
us=0#user score counter
cs=0#computer score counter
dr=0#draw counter
while(x):


    list1=["s","w","g"]
    print("Enter s for Snake:")
    print("Enter w for Water:")
    print("Enter g for gun:")

    ch1=input()
    ch2=random.choice(list1)

    if(ch1=="s" and ch2=="w" or ch1=="w" and ch2=="g" or ch1=="g" and ch2=="s"):
        us=us+1
        print(" you win and your score is-",us)
    elif (ch2 == "s" and ch1 == "w" or ch2 == "w" and ch1 == "g" or ch2 == "g" and ch1 == "s"):
        cs = cs + 1
        print(" computer wins and computer's score is-", cs)
    else:
        dr=dr+1
        print("this match is draw and total number of draws are-",dr)

    x=x-1
    if(x>0):
        print("Number of rounds remaining",x)

if(us>cs):
    print("you win the game")
elif(cs>us):
    print("computer wins the game")
else:
    print("the game is draw")