x="romeo"
def a():

    global x
    x = "juliet"
    print("the value of x is" + x)

def updown():
    for i in range(5,-11,-1):
        print(i*i-1)

updown()