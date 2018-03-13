import random
def list_random():
    list_random = []
    for i in range(1,11):
        num=random.randint(1,10)
        list_random.append(num)
    return list_random
nums=list_random()
print(nums)
