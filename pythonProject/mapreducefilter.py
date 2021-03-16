# ------------------------------maping---------------
# l1=["1","2"]
# x=list(map(lambda x:int(x)*10,l1))
# print(x)



# def sqare(x):
#     return x*x
# def cube(x):
#     return x*x*x
#
# f1=[sqare,cube]
#
# for i in range(10):
#     x=list(map(lambda x: x(i),f1))
#     print(x)
# ----------------------------filter-------------------------

# list1=["riya","rita","miya","maysa","money"]
#
# def check_name(x):
#     if(x.startswith('m') and x.endswith('a')):
#       return x
#
# val=list(filter(check_name,list1))
# print(val)

# ------------------------------reduce------------------------

# from functools import reduce
# lis1=[1,2]
# val=reduce(lambda x,y: (x+1)+(y+1),lis1 )
# print(val)
