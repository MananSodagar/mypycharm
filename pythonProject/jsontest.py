import json

#
# with open("json1.json") as f:
#     x=json.load(f)
#
#
# for i in x:
#     print(i,x[i])
#
# print(type(x))


x={"name":"manan","age":30,"sex":"male","married":"False"}
y=json.dumps(x,indent=5,separators=("+","="),sort_keys="True")
print(type(y))