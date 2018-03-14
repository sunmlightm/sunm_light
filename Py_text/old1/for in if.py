phone=[{'brand':'oppo'},{'brand':'vivo'},{'brand':'huawei'}]
phone_input=input('请输入手机型号：')
have=0
for phone_item in phone:
    brand=phone_item.get('brand')
    if brand==phone_input:
        have=1
        break
if have==0:
    phone_new = {}
    phone_new['brand'] = phone_input
    phone.append(phone_new)
else:
    print('该手机已存在')
print(phone)