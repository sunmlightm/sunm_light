print("="*50)
print("\tcard manage System5.0")
print("\t1.add new card")
print("\t2.delete card")
print("\t3.update card")
print("\t4.search card")
print("\t5.exit System")
print("="*50)
card_info=[{"name":"pengcheng","qq":"10000","weixin":"pengcheng_niu"},
{"name":"yulei","qq":"10001","weixin":"yulei_shuai"}]
while True:
    number=int(input("请选择（1~5）:"))
    if number==1:
        card_add={}
        card_add["name"]=input("请输入名字")
        card_add["qq"]=input("请输入qq号")
        card_add["weixin"]=input("请输入微信号")
        card_info.append(card_add)
        print(card_info)
    elif number==2:
        name=input("请输入一个名字")
        for card in card_info:
            if name==card.get("name"):
                card_info.remove(card)
                print(card_info)
    elif number==3:
        name=input("请输入需要修改的名字")
        upda_name=input("请输入修改之后的名字")
        upda_qq=input("请输入更正之后的qq")
        upda_weixin=input("请输入更正之后的微信")
        for card in card_info:
            if name==card.get("name"):
                card["name"]=upda_name
                card["qq"]=upda_qq
                card["weixin"]=upda_weixin
                print(card_info)
    elif number==4:
        name = input("请输入需要寻找的名字")
        flg=0
        for card in card_info:
            if name==card['name']:
                print(card)
                flg=1
            
        if flg==0:print("sorry，没有搜索到此名")
    elif number==5:
        break

