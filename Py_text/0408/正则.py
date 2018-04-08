import re
num="010-12345678"

re_obj=re.match("([0]\d{2,3})-([1-9]\d{7})",num)

print(re_obj.group())
print(re_obj.groups())