class Road(object):
    def __init__(self,name,length):
        self.name=name
        self.length=length
class Car(object):
    def __init__(self,name,sp_h):
        self.name = name
        self.sp_h = sp_h
    def get_time(self,road):
        time=road.length/self.sp_h
        print("预计会在%s上行驶%d小时"%(road.name,time))
    def __str__(self):
        msg="name:"+self.name+" 车速是:"+str(self.sp_h)+"Km/h"
        return msg
road=Road("国道115",1000)
car=Car("car1",100)
car.get_time(road)
print(car)