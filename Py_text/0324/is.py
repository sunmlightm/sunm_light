str1="hello"
str2="hello"
str3="hello"

print(id(str1))
print(id(str2))
print(id(str3))
str1="helloworld"
str2=str1
str3="helloworld"
print(str1 is str3)

list1=[1,2,3,4]
list2=list1
list3=[1,2,3,4]
print(">>>>",list1 is list2)
print(list1 is list3)
print(list2 is list3)
print(list1==list2==list3)

num1=33333333333333333333
num2=33333333333333333333
print(num1 is num2)