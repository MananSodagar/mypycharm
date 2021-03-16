print("HOWmany Items do you want to enter")
x=int(input())

ls=[]
dt={}
st=()


for i in range(x):
    x=input(f"You are enterring {i}number of Items >=")
    ls.append(x)
    dt.append(x)
    st.append(x)

print(st)


