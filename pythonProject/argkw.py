
# the normal argument comes first,
# then comes args and after that comes kwargs
def frienddt(*args):
    for i in args:
        print(f"the name is {i}")


st={"manan","raj","yash","gani"}
frienddt(*st)

def frienddt(**args):
    for i,j in args.items():
        print(f"the name is {i} and rank is {j}")


st={"manan":1,"raj":2,"yash":3,"gani":4}
frienddt(**st)