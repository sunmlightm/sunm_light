import random
def list_random():
    list_random = []
    num = random.randint(1, 50)
    flg=0
    if len(list_random)!=0:
        for it in list_random:
            if num==it:
                flg=1
                continue
    if flg==0:
        list_random.append(num)
nums=list_random()
print(nums)