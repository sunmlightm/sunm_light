class ShoeFactory(object):
    def shoe_type(self,type):
        if type=="sport":
            return Sport()
        if type=="climbing":
            return Climbing()


class Shoes(object):
    def walk(self):
        print("walking... ...")

class Sport(Shoes):
    def __init__(self):
        self.type="sport"


class Climbing(Shoes):
    def __init__(self):
        self.type = "climbing"


shoe_fac=ShoeFactory()
