import time
avg1=0.00000000
avg2=0.00000000
for i in range(10000):

    in1=time.time()


    # for i in range(10):
    #     print()
    x = 0
    while (x < 10):
        print()
        x += 1

    in2 = time.time()
    avg1=avg1+(in2-in1)


    win1=time.time()

    for i in range(10):
        print()
    # x=0
    # while(x<10):
    #     print()
    #     x+=1
    win2=time.time()

    avg2 = avg2 + (win2 - win1)


    print(avg1)
    print(avg2)




