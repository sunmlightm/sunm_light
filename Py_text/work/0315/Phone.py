class Phones(object):
    def __init__(self,brand,type):
        self.brand=brand
        self.type=type
    def show_info(self):
        print("手机品牌是%s,型号是%s"%(self.brand,self.type))
    def call(self):
        print("使用%s品牌%s型号的手机正在打电话"%(self.brand,self.type))

phone_a=Phones("华为","mate10")
phone_a.show_info()
phone_a.call()