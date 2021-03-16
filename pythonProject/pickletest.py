import pickle
import bz2

mydict={"name":"manan","age":30,"sex":"male","married":"False"}
#
#
# file1="mypickle1"
# fileobj= open(file1,"wb")
#
#
# pickle.dump(mydict,fileobj)


file="mypickle2"

file1= open(file,"wb")
#
# y=pickle.load(file1)
#
# print(type(y))

a=bz2.BZ2File(file1)

pickle.dump(mydict, file1)

file1.close()