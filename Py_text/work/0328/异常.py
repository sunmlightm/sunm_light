dic={"name":"zhuang","age":18}
# print(dic.pop("name"))
print(dic["name"])
print(dic.get("name"))
for value in dic.values():
	print(value)

for key in dic.keys():
	print(key)

for value in dic.items():
	print(value)