list1=["a",[1,2,3,4,5,6,7,8,9],"b",11,22,4,5,7,True ]
list1.reverse()
x=list()
for item in list1:
    if str(item).isnumeric() and item>6:
