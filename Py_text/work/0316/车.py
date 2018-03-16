class Vehicle(object):
    def __init__(self,color,speed):
        self.color=color
        self.speed=speed
    def stop(self):
        print("%s:车停了"%self.type)
    def move(self):
        print("%s:GO!!"%self.type)
class Bike(Vehicle):
    type="bike"
class Car(Vehicle):
    type="car"

bike=Bike("black","20km/h")
bike.stop()
car=Car("red","100Km/h")
car.move()