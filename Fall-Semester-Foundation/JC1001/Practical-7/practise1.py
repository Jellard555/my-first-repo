class Vehicle:
    def __init__(self,ms,mileage):
        self.ms = ms
        self.mileage = mileage
    def discription(self):
        long_name = f"{self.ms} {self.mileage}"
        return long_name.capitalize()
    def name(self,name):
        print(f"这只车叫{name}")
    def seating_capacity(self,quantity):
        print(f"这个交通工具可以坐{quantity}个人")
vehicle1 = Vehicle(80,455)
vehicle1.seating_capacity(455)
print(f"The max speed is {vehicle1.ms},and it can work over {vehicle1.mileage} miles")
class Bus(Vehicle):
    def __init__(self,ms,mileage):
        super().__init__(ms,mileage)
for_bus = Bus(80,550)
print (for_bus.discription())

    