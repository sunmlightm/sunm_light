list_num=[9,10,30,30,11,0,12,0]
num_min = list_num[0]
num_max = list_num[0]
i=1
while i<len(list_num):
    if num_min>list_num[i]:
        num_min=list_num[i]
    if num_max<list_num[i]:
        num_max=list_num[i]
    i+=1
print('最小值是：%d,最大值是：%d'%(num_min,num_max))