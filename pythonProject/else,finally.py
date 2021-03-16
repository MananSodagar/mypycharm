try:
   i=int(input())
except Exception as e:
    print(e)
else:
    print("every thing is good")
finally:
    print("the entered number is")