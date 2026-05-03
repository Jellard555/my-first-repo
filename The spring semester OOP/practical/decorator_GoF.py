class Car:
    def assemble(self): pass
class BasicCar(Car):
    def assemble(self):
        print("Basic Car")

class CarDecorator(Car):
    def __init__(self,car):
        self.car = car
    def assemble(self):
        self.car.assemble()

class SportsCar(CarDecorator):
    def assemble(self):
        super().assemble()
        print("Adding features of Sports Car")

@SportsCar
def sports_car(): 
    SportsCar(BasicCar())
sports_car.assemble()