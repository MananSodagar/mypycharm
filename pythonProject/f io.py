x=open("filesiopractice","rt") #opening and assigning the file
# myfile=x.read() #reading the file
# myfile=x.readline() #reads only single line

# prints 50 character from myflie
# myfile=x.read(50)#  reads firts 50 char
# for line in myfile:
#         print(line, end=("_"))

# reads every line from file using forloop dont read it when you do this, because it emptys file pointer
for line in x:
        print(line, end=("_"))



# myfile=x.read(5)# reads 5 char after 50
# print(myfile)
#
# myfile=x.read()
# print(myfile)

x.close()# closing is most important