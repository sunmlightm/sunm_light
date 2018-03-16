class Home:
    def __init__(self,area,info):
        self.area=area #房子面积
        self.info=info #房子描述
        self.left_area=area #剩余面积
        self.contain_items=[] #全部的家具

    def __str__(self):
        msg = "房子面积是:" + str(self.area) + ",描述:" + self.info + ",剩余面积:" + str(self.left_area)
        msg += ",家具有:["
        for x in range(len(self.contain_items)):
            # print(self.contain_items[x].get_name())
            # # print(name)
            if (x == len(self.contain_items) - 1):
                msg += self.contain_items[x].get_name() + "]"
            else:
                msg += self.contain_items[x].get_name() + ","

        return msg

    def add_item(self,item):
        print("面积是:",item.area)
        self.left_area = self.left_area - item.area
        self.contain_items.append(item)


class Sofa(object):

    def __init__(self,name,area):
        self.name=name
        self.area=area

    def __str__(self):
        msg="家具的名称:"+self.name+",占用面积:"+str(self.area)
        return msg

    def get_name(self):
        return self.name



class Bed:

    def __init__(self,area,type):
        self.name="床"
        self.area=area
        self.type=type

    def __str__(self):
        msg="家具的名称:"+self.name+",类型:"+self.type+",占用面积:"+str(self.area)
        return msg

    def get_name(self):
        return self.name
class Refrigerator(object):
    def __init__(self,area):
        self.name="冰箱"
        self.area=area
    def __str__(self):
        msg="家具的名称:"+self.name+",占用面积:"+str(self.area)
        return msg
    def get_name(self):  
        return self.name
#使用过程
home=Home(120,"三室一厅")
print(home)
#买家具
sofa=Sofa("沙发1",5)
print(sofa)
#将沙发放到家
home.add_item(sofa)
print(home)
#买床
bed=Bed(4,"席梦思")
home.add_item(bed)
print(home)
sofa2=Sofa("沙发2",10)
home.add_item(sofa2)
print(home)
bingxaing=Refrigerator(1)
home.add_item(bingxaing)
print(home)
