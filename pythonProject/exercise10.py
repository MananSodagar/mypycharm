import pickle
x=[]
a=[]
b=[]
c=[]
z=[]

with open("iris.txt", "r") as f:
    for i in f:
         x.append(i.strip())
    for i in x:
        if i.endswith("Iris-setosa"):
            a.append(i)
        elif i.endswith("Iris-versicolor"):
            b.append(i)
        elif i.endswith("Iris-virginica"):
            c.append(i)
z=[a,b,c]
openfile=open("iris_list","wb")
pickle.dump(z,openfile)
openfile.close()

readfile=open("iris_list","rb")
readingpickle=pickle.load(readfile)

print(readingpickle==z)






