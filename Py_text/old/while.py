phone=[{'brand':'oppo'},{'brand':'vivo'},{'brand':'huawei'}]
phone_input=input('请输入手机型号：')
i=0
while i<len(phone):
    brand=phone[i].get('brand')
    if brand==phone_input:
        break
    i += 1
if i==len(phone):
    phone_new = {}
    phone_new['brand'] = phone_input
    phone_new['price'] = int(input('请输入价格'))
    phone.append(phone_new)
else:
    print('该手机已存在')
print(phone)