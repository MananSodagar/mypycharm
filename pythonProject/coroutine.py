def reader():
    import time
    book="123455r4wefnoiergvnioergoeirgreouhgoudrhgiudrhgiheriughreih reherohgrhegoueriu msnsnbijvberuf manan"
    time.sleep(2)


    while 1:
        x=yield
        if x in book:
            print("yes")
        else:
            print("no")


r=reader()
next(r)
r.send("manan")
r.send("123")
r.send("xxx")
r.send(input())